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
        self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)

        # GETTING THE ANGLES
        # self.joint_sub = rospy.Subscriber('joint_states', JointState, self.joint_state_callback)
        self.head_sub = rospy.Subscriber("/tactile_touch", HeadTouch, self.headtouch_callback)

        self.botharms = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw",
                            "LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]

        self.joint_sequence_start = self.motionProxy.getAngles(self.botharms, True) # names , useSensors
        print("Initial Position Recorded")
        print("Place the hand on the joystick and press head button")
        self.joint_sequence_end = []
        self.headtouch = HeadTouch(0,0) # Init Headtouch message as empty

        ## Camera for fine grasping
        self.tflistener = tf.TransformListener()
        self.tfbroadcaster = tf.TransformBroadcaster()


        # SET INIT POSITION WITH EVERYTHING STIFF BUT NOT ARMS
        self.postureProxy = ALProxy('ALRobotPosture', naoIP, 9559)
        self.postureProxy.goToPosture("Crouch", 1.0)
        self.rate.sleep()
        # self.motionProxy.openHand("LHand")
        # self.motionProxy.openHand("RHand") 
        self.motionProxy.setStiffnesses(self.botharms, [0.0 for i in self.botharms])


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
        self.setStickCartesianCoordinate()


    def callback_img(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.imshow("Bottom Camera", cv_image)
        cv2.waitKey(3)

    def run(self): 
        # Position the Nao 
        # Let press the Head Button to start joint recording 
        self.setStickCartesianCoordinate()
        if self.headtouch.button is 1 and self.headtouch.state is 1:
            self.joint_sequence_end = self.motionProxy.getAngles(self.botharms, True)
            print(self.joint_sequence_end)
            print("Hand and joystick is recorded.")

            # (trans,rot) = self.tflistener.lookupTransform("/ARUCOFRAME","/CameraBottom_optical_frame",rospy.Time(0))
            # print("Trans Rot of Arcuo from Camera ") 
            # print(trans,rot)           
            # (trans,rot) = self.tflistener.lookupTransform("/l_gripper","/ARUCOFRAME",rospy.Time(0))
            # print("Trans Rot of left stick from Aruco ")            
            # print(trans,rot)
            # (trans,rot) = self.tflistener.lookupTransform("/r_gripper","/ARUCOFRAME",rospy.Time(0))
            # print("Trans Rot of RIGHT stick from Aruco ")            
            # print(trans,rot)

        # Write these joint state into a file (So we could update this in the future-- Calibration)    

        # Reset the state
        # Release everything 
        if self.headtouch.button is 2 and self.headtouch.state is 1: 
            print("Relax")
            self.motionProxy.killAll()
            self.motionProxy.setStiffnesses(self.botharms, [0.0 for i in self.botharms])
            time.sleep(0.05)
            self.motionProxy.setStiffnesses(["RHand","LHand"], [0.0,0.0])
            # self.motionProxy.closeHand("LHand")
            # self.motionProxy.openHand("RHand")
            print("done relaxing")

        if self.headtouch.button is 3 and self.headtouch.state is 1: 
            print("head button 3 is press")
            # self.send_cartesian_movement()
            # self.motionProxy.setAngles("RArm", 1.0, 1.0)

            ## RUN LIFTING SEQUENCE 
            self.lifting_sequence()

    def getHomoMat(self,trans, angles):
        scale = None
        shear = None
        perspective = None

        return tf.transformations.compose_matrix(scale, shear, angles, trans, perspective)


    # def getTransRot(self,mat):
    #     scale = None
    #     shear = None
    #     perspective = None


    #     return tf.transformations.compose_matrix(scale, shear, angles, trans, perspective)
            
    def setStickCartesianCoordinate(self):
        # Trans Rot of Arcuo from Camera --- THIS ONE CHANGE EVERY TIME
        tarAruco_Camera = [[-0.00845721015460802, 0.1552655403581574, 0.093520057441842], [0.9346952718857345, -0.03283636130211642, 0.0021888805934734187, 0.3539233404180027]]
        # Trans Rot of left stick from Aruco 
        tarLStick_Aruco =([-0.0017675604682759471, -0.008507536697413859, -0.08253574729763671], [-0.8046676307743155, 0.18555869257733368, 0.49836954079581575, -0.2640185152598363])
        # Trans Rot of RIGHT stick from Aruco 
        tarRStick_Aruco = ([-0.030505818136187163, -0.0646244809682456, -0.015516809471004755], [0.22916915525623704, 0.7602480060467611, -0.19366677793477247, -0.5761923695307235])

        # HAruco_Camera = self.getHomoMat(trans=tarAruco_Camera[0], angles=tarAruco_Camera[1])
        # HLStick_Aruco = self.getHomoMat(trans=tarLStick_Aruco[0], angles=tarLStick_Aruco[1])
        # HRStick_Aruco = self.getHomoMat(trans=tarRStick_Aruco[0], angles=tarRStick_Aruco[1])

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
        

        # tf.transformations.euler_from_quaternion(quaternion, axes='sxyz') 
        
               
        # HAruco_tf.transformations.concatenate_matrices()

        # do the action and grab the stick 
        # lift the stick to starting position, 
        # check the camera to see where the stick is, 
        # if the glob center is where we expected, move on 
        # if it's not then asking for reposition. 
    
    def getStickTargetFromTorso(self):
        # REturn position 0 is left and rotation 1 is right 
        (ltrans,lrot) = self.tflistener.lookupTransform("/LStick","/torso",rospy.Time(0))
        (rtrans,rrot) = self.tflistener.lookupTransform("/RStick","/torso",rospy.Time(0))


        self.tfbroadcaster.sendTransform(
                    translation=ltrans, 
                    rotation= lrot, 
                    time = rospy.get_rostime(),
                    child = 'LTARGETLTARGET',
                    parent= 'torso')

        ####
        # This is is the only one that have the correct frame
        # 
        #             
        self.tfbroadcaster.sendTransform(
                    translation=rtrans, 
                    rotation= rrot, 
                    time = rospy.get_rostime(),
                    child = 'RTARGETTARGET',
                    parent= 'torso')        

        # TODO: TURN THIS INTO TRANSFORM 

        # chainName        = "Torso"
        # frame            = motion.FRAME_ROBOT
        # transform        = [1.0, 0.0, 0.0, 0.00,
                        # 0.0, 1.0, 0.0, 0.00,
                        # 0.0, 0.0, 1.0, 0.25]
        # fractionMaxSpeed = 0.2
        # axisMask         = 63
        # self.motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)



        # return [[ltrans[0],ltrans[1],ltrans[2],0,0,0],[rtrans[0],rtrans[1],rtrans[2],0,0,0]]\
        print("L trans {}".format(ltrans))
        


        return ltrans,lrot


    def lifting_sequence(self):
        self.motionProxy.setStiffnesses(self.botharms, [1.0 for i in self.botharms])
        ### Motion proxy set transform 

        self.send_movement(self.postureFlyingEagles,1.0, True)
        print("sent flying movement")
        self.send_movement(self.postureHandInTheAir,3.0, True)
        self.send_movement(self.postureHandReadyForStick,3.0, True)
        self.open_hand()
        # self.send_movement(self.postureHandOnStick,3.0, True)#
        # TODO: Fine tune location 
        # fractionMaxSpeed = 0.2
        # axisMask = 7 # position is probably enough
        # endeffectorChain = ["RArm"] 
        frame = motion.FRAME_TORSO
        ltrans, lrot = self.getStickTargetFromTorso()
        print("TARGET ltrans Position {}".format(ltrans))
        target = ltrans
        print("TARGET Position {}".format(target))
        # self.motionProxy.setPositions(endeffectorChain, frame, target[1], fractionMaxSpeed, axisMask)
        self.tfbroadcaster.sendTransform(
            translation=target, 
            rotation= lrot, 
            time = rospy.get_rostime(),
            child = 'RTARGET',
            parent= 'torso')
        ####3
        print("sent other movement")
        self.close_hand()
        # self.send_movement(self.postureLiftStick,2.0, True)
    
    
    def close_hand(self):
        self.motionProxy.setStiffnesses("RHand", 1.0)
        self.motionProxy.setStiffnesses("LHand", 1.0)
        self.motionProxy.setAngles("LHand", 0.0, 1.0)
        self.motionProxy.setAngles("RHand", 0.0, 1.0)
                
    def open_hand(self):
        self.motionProxy.setStiffnesses("RHand", 1.0)
        self.motionProxy.setStiffnesses("LHand", 1.0)
        self.motionProxy.setAngles("LHand", 1.0, 1.0)
        self.motionProxy.setAngles("RHand", 1.0, 1.0)

    def headtouch_callback(self, headtouch):
        self.headtouch = headtouch   

    def get_pose_from_mat(self, mat):
        # scale, shear, angles, trans, persp = decompose_matrix(S)
        _,_,angles, trans,_ = tf.transformations.decompose(mat)
        # Check the output of this pose to see if it's correct 
        return list(trans,angles)

##############
# SEND MOVEMENT TO NAO 
##############

    def send_cartesian_movement(self):
        # Let's think about the franme that we need to control from 
        # Should be from the torso
        frame = motion.FRAME_TORSO
        effectorList = []
        pathList = []
        axisMastList = [motion.AXIS_MASK_VEL, motion.AXIS_MASK_VEL]
        timeList = [[1.0],[1.0]]

        # Could use another approach and get the current position first then
        # gradually correct it.
        effectorList.append("LArm")
        ##

        ## TODO: This append need to have take in a vector 
        pathList.append(self.get_pose_from_mat(self.handle_of_stick()))

        # ONe of this will not return correctly because we're getting not adjustment for 
        # both of the arm at the moment 
        effectorList.append("RArm")
        pathList.append(self.get_pose_from_mat(self.handle_of_stick()))

        self.motionProxy.positionInterpolations(effectorList, frame, pathList, 
                                    axisMastList, timeList)


    def send_movement(self,position,speed, stay_stiff=True):
        '''send each joint to the robot. Use a non-blocking call to the API
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


        return True


    def get_aruco_frame(self):
        try: 
            (trans,rot) = self.tflistener.lookupTransform("/CameraBottom_optical_frame","/ARUCOFRAME",rospy.Time(0))
                # print("aruco thingy")
            print(trans,rot)
            # There is no translattion here 
            # H_aruco_to_opticalcamera = tf.transformations.euler_matrix(rot[0],rot[1],rot[2])
            H_aruco_to_opticalcamera = tf.transformations.compose_matrix(angles=rot, translate=trans)
            # H_opticalcamera_to_camera = tf.transformations.euler_matrix(-math.pi/2,0.0,-math.pi/2)
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


    def handle_of_stick(self):
        aruco_torso = self.get_aruco_frame()
        # TODO: add the right hand adjustment for each hand
        hand_adjustment = tf.transformations.compose_matrix(translate=[0,0,0])
        handle_world = aruco_torso - hand_adjustment
        return handle_world
    
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
