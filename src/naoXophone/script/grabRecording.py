#!/usr/bin/env python

import rospy
import sys
from sensor_msgs.msg import JointState
import os 
import qi
from naoqi import ALProxy
from naoqi_bridge_msgs.msg import HeadTouch
import tf
import numpy as np
import math
import motion
import time
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


# roslauch nao_apps tactile.launch
# docs: http://doc.aldebaran.com/2-4/naoqi/motion/control-joint-api.html 
# carteasian control http://doc.aldebaran.com/2-1/naoqi/motion/control-cartesian.html
# http://doc.aldebaran.com/2-1/naoqi/motion/control-cartesian-api.html#ALMotionProxy::positionInterpolations__AL::ALValueCR.AL::ALValueCR.AL::ALValueCR.AL::ALValueCR.AL::ALValueCR
# http://docs.ros.org/en/jade/api/tf/html/python/transformations.html

naoIP = str(os.getenv("NAO_IP"))

class grabSticks:
    def __init__(self):
        self.TROUBLESHOOT = True
        
        self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)

        # GETTING THE ANGLES
        # self.joint_sub = rospy.Subscriber('joint_states', JointState, self.joint_state_callback)
        self.head_sub = rospy.Subscriber("/tactile_touch", HeadTouch, self.headtouch_callback)

        self.botharms = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw",
                            "LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]

        self.headtouch = HeadTouch(0,0) # Init Headtouch message as empty

        ## SETHANDSPEED
        self.hand_speed = 0.5
        ## Camera for fine grasping
        self.tflistener = tf.TransformListener()
        self.tfbroadcaster = tf.TransformBroadcaster()

        # PREDEFINE POSTURES 
        self.postureFlyingEagles = [1.5355758666992188, -1.2717280387878418, 0.8988821506500244, 0.24701595306396484, 0.8528621196746826, 1.6980960369110107, 1.1611961126327515, -1.2333779335021973, -0.2269899845123291, -0.6029040813446045]
        self.postureHandInTheAir = [-1.4357820749282837, -0.3528618812561035, 0.46169209480285645, 0.6688659191131592, -0.14883995056152344, -1.6214799880981445, 0.42180800437927246, -0.07827591896057129, -0.7930359840393066, 0.11961007118225098];
        self.postureHandOnStick = [0.6458559036254883, 0.0060939788818359375, 0.9402999877929688, 0.76857590675354, 0.5092461109161377, 0.6411700248718262, -0.09821796417236328, -0.9127721786499023, -0.5798101425170898, -0.49859189987182617]
        self.postureHandReadyForStick = [1.0508317947387695, -0.1304318904876709, 1.8024080991744995, 1.092249870300293, 0.0827939510345459, 1.084496021270752, 0.17176604270935059, -1.960494041442871, -1.1029040813446045, 0.11961007118225098]
        self.postureLiftStick = [0.38507604598999023, 0.03217196464538574, 1.010864019393921, 0.76857590675354, 0.6718499660491943, 0.309826135635376, -0.10895586013793945, -0.9833359718322754, -0.5782761573791504, -0.6443219184875488]

        # SUBSCRIBERS FOR IMAGES
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback_img)

        
        # SET stick cartesian coordinate in relation to aruco 
        self.setInitialPose()
        self.setStickCartesianCoordinate()

    def setInitialPose(self):
        # SET INIT POSITION WITH EVERYTHING STIFF BUT NOT ARMS

        self.postureProxy = ALProxy('ALRobotPosture', naoIP, 9559)
        self.postureProxy.goToPosture("Crouch", 1.0)
        self.rate.sleep()
        if self.TROUBLESHOOT:
            self.motionProxy.setStiffnesses(self.botharms, [0.0 for i in self.botharms])
            self.motionProxy.setStiffnesses("Head", [0.0,0.0])


    def callback_img(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.imshow("Bottom Camera", cv_image)
        cv2.waitKey(3)


    def run(self): 
        if self.headtouch.button is 1 and self.headtouch.state is 1:
            self.joint_sequence_end = self.motionProxy.getAngles(self.botharms, True)
            print(self.joint_sequence_end)
            print("Hand and joystick is recorded.")

        if self.headtouch.button is 2 and self.headtouch.state is 1: 
            print("Relax")
            self.motionProxy.killAll()
            self.motionProxy.setStiffnesses(self.botharms, [0.0 for i in self.botharms])
            time.sleep(0.05)
            self.motionProxy.setStiffnesses(["RHand","LHand"], [0.0,0.0])
            print("done relaxing")

        if self.headtouch.button is 3 and self.headtouch.state is 1: 
            print("head button 3 is press")
            ## RUN LIFTING SEQUENCE 
            self.lifting_sequence()

        try:
            self.getStickTargetFromTorso()
        except:
            pass


    def showRelativeTxStickfromAruco(self):
        ''' Pull the transformation from the right hand and left hand to aruco 
        USE THIS FOR CALIBRATION 
        ''' 
        (ltrans,lrot) = self.tflistener.lookupTransform("/ARUCOFRAME","/l_gripper",rospy.Time(0))
        print("Trans Rot of LEFT stick from Aruco {}".format([ltrans,lrot]))            

        (rtrans,rrot) = self.tflistener.lookupTransform("/ARUCOFRAME","/r_gripper",rospy.Time(0))
        print("Trans Rot of RIGHT stick from Aruco {}".format([rtrans,rrot]))            

            
    def setStickCartesianCoordinate(self):
        '''Establish the coordinate Frame of the stick inrelation with aruco
        TODO: CALIBRATE USING self.showRelativeTxStickfromAruco()
        '''
        tarAruco_Camera = [[-0.00845721015460802, 0.1552655403581574, 0.093520057441842], [0.9346952718857345, -0.03283636130211642, 0.0021888805934734187, 0.3539233404180027]]

        tarLStick_Aruco = [[-0.072581625212525, 0.12116529787387573, 0.011517758344727458], [0.8307618848915851, -0.12058925456751696, -0.5042605497068606, -0.20251967880570315]]
        tarRStick_Aruco = [[0.020874788973296116, 0.13886821514641357, 0.007092554727019779], [-0.2805590210808618, -0.7528074109481558, 0.3172331261893348, -0.5039154506063729]]

        # Broadcast the static transformation
        self.tfbroadcaster.sendTransform(
                    translation=tarRStick_Aruco[0], 
                    rotation= tarRStick_Aruco[1], 
                    time = rospy.get_rostime(),
                    child = 'RStick',
                    parent= 'ARUCOFRAME')
        self.tfbroadcaster.sendTransform(
                    translation=tarLStick_Aruco[0], 
                    rotation= tarLStick_Aruco[1], 
                    time = rospy.get_rostime(),
                    child = 'LStick',
                    parent= 'ARUCOFRAME')
        

    def getStickTargetFromTorso(self):
        '''Re-establish position of the sticks relative to NAO's toso frame'''

        (ltrans,lrot) = self.tflistener.lookupTransform("/torso","/LStick",rospy.Time(0))
        (rtrans,rrot) = self.tflistener.lookupTransform("/torso","/RStick",rospy.Time(0))

        self.ltrans = ltrans
        self.lrot = lrot 
        self.rtrans = rtrans
        self.rrot = rrot 


    def lifting_sequence(self):

        ## TODO: make cartesian control for both arms
        self.motionProxy.setStiffnesses(self.botharms, [1.0 for i in self.botharms])
        ### Motion proxy set transform 

        self.send_movement(self.postureFlyingEagles,1.0, True)
        print("sent flying movement")
        self.send_movement(self.postureHandInTheAir,3.0, True)
        self.send_movement(self.postureHandReadyForStick,3.0, True)
        self.open_hand()
        time.sleep(1)
        self.send_movement(self.postureHandOnStick,3.0, True) 
        #########
        # self.send_cartesian_armmovement(0.8,stay_stiff=True)
        #########
        self.close_hand()
        self.send_movement(self.postureLiftStick,2.0, True)
        print("finishing lift sequence")
    
    def close_hand(self):
        
        self.motionProxy.setStiffnesses("RHand", 1.0)
        self.motionProxy.setStiffnesses("LHand", 1.0)
        self.motionProxy.setAngles("LHand", 0.0, self.hand_speed)
        self.motionProxy.setAngles("RHand", 0.0, self.hand_speed)
                
    def open_hand(self):
        self.motionProxy.setStiffnesses("RHand", 1.0)
        self.motionProxy.setStiffnesses("LHand", 1.0)
        self.motionProxy.setAngles("LHand", 1.0, self.hand_speed)
        self.motionProxy.setAngles("RHand", 1.0, self.hand_speed)

    def headtouch_callback(self, headtouch):
        self.headtouch = headtouch   


##############
# SEND MOVEMENT TO NAO 
##############

    def get_pose_from_mat(self, mat):
        # scale, shear, angles, trans, persp = decompose_matrix(S)
        _,_,angles, trans,_ = tf.transformations.decompose(mat)
        # Check the output of this pose to see if it's correct 
        return list(trans,angles)
    def send_cartesian_armmovement(self, speed, stay_stiff=True):
        # Let's think about the franme that we need to control from 
        # Should be from the torso
        fractionMaxSpeed = 0.8
        axisMask = 7 # position is probably enough  NOTE bit flipping 
        endeffectorChain = ["LArm", "RArm"] 
        frame = motion.FRAME_TORSO
        targetL = [self.ltrans[0], self.ltrans[1], self.ltrans[2], 0, 0, 0]
        targetR = [self.rtrans[0], self.rtrans[1], self.rtrans[2], 0, 0, 0]
        target = [targetL, targetR]
        self.motionProxy.setPositions(endeffectorChain, frame, target, fractionMaxSpeed, axisMask)         #
        if not stay_stiff: 
            self.motionProxy.setStiffnesses(self.botharms, [0.0 for i in self.botharms])


    def send_movement(self,position,speed, stay_stiff=True):
        '''send each joint to the robot. Use a BLOCKING call to the API
            Input the final position that we want the robot to be in 
            Specify weather or not the robot should stay stiff afterwards.
        '''

        # http://doc.aldebaran.com/1-14/naoqi/motion/control-joint-api.html#ALMotionProxy::angleInterpolationWithSpeed__AL::ALValueCR.AL::ALValueCR.floatCR
        # Send with angle interpolation with speed 
        self.motionProxy.setStiffnesses(self.botharms, [1.0 for i in self.botharms])
        
        timeList = [speed for i in range(len(self.botharms))]
        isAbsolute = True
        self.motionProxy.angleInterpolation(self.botharms, position,timeList, isAbsolute)
        
        # Send with motionProxy
        # fractionMaxSpeed = 0.1
        # self.motionProxy.setAngles(self.botharms, position, fractionMaxSpeed)

        if not stay_stiff: 
            self.motionProxy.setStiffnesses(self.botharms, [0.0 for i in self.botharms])


    def get_aruco_frame(self):
        try: 
            (trans,rot) = self.tflistener.lookupTransform("/CameraBottom_optical_frame","/ARUCOFRAME",rospy.Time(0))

            H_aruco_to_opticalcamera = tf.transformations.compose_matrix(angles=rot, translate=trans)
            H_opticalcamera_to_camera = tf.transformations.compose_matrix(angles=[-math.pi/2,0.0,-math.pi/2])
            H_aruco_to_camera  = np.matmul(H_aruco_to_opticalcamera, H_opticalcamera_to_camera)

            print("H_aruco_to_camera \n {}".format(H_aruco_to_camera))
            self.broadcast_target_tf("/CameraBottom_frame", "/aruco_to_camera", H_aruco_to_camera)
            
            useSensorValues=True
            H_camera_to_torso = self.motionProxy.getTransform("CameraBottom",
                                motion.FRAME_TORSO, useSensorValues)
            H_camera_to_torso = np.asarray(H_camera_to_torso).reshape([4,4])
            print("H_camera_to_torso \n {}".format(H_camera_to_torso))           
            self.broadcast_target_tf("/torso", "/camera_to_torso", H_camera_to_torso)
            
            H_aruco_to_torso = np.matmul(H_aruco_to_camera,H_camera_to_torso )
            print("H_aruco_to_torso \n {}".format(H_aruco_to_torso))
            return H_aruco_to_torso   

        except tf.LookupException: 
            pass
            return np.identity(4)

    
    def broadcast_target_tf(self, parent_frame, child_frame, homogeneous_mat):
        rvec = tf.transformations.euler_from_matrix(homogeneous_mat)
        tvec = homogeneous_mat[:3,3]
        self.tfbroadcaster.sendTransform(
                translation=tvec.squeeze(), 
                rotation= tf.transformations.quaternion_from_euler(rvec[0], rvec[1], rvec[2]), 
                time = rospy.get_rostime(),
                child = child_frame,
                # parent = 'TOPCAMERAFRAME')
                parent= parent_frame)

def main():
    # TODO: ESTABLISH THE JOINT LIMITS? 

    rospy.init_node('grabSticks', anonymous=True)
    nao_grab_stick = grabSticks()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_grab_stick.run()
        rate.sleep()



if __name__ == '__main__':
	main()
