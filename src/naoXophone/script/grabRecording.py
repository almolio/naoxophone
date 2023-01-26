#!/usr/bin/env python

import rospy
import sys
from sensor_msgs.msg import JointState
import os 
import qi
import argparse
from naoqi import ALProxy
from naoqi_bridge_msgs.msg import HeadTouch
import tf
import numpy as np
import math
import motion

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

        self.rightarm = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
        self.leftarm = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
        # self.botharms = [*self.rightarm, *self.leftarm]
        self.botharms = self.leftarm
        self.joint_sequence_start = self.motionProxy.getAngles(self.botharms, True) # names , useSensors
        print("Initial Position Recorded")
        print("Place the hand on the joystick and press head button")
        self.joint_sequence_end = []
        self.headtouch = HeadTouch(0,0) # Init Headtouch message as empty

        ## Camera for fine grasping
        self.tflistener = tf.TransformListener()
        self.tfbroadcaster = tf.TransformBroadcaster()


    def run(self): 
        # Position the Nao 
        # Let press the Head Button to start joint recording 
        if self.headtouch.button is 1 and self.headtouch.state is 1:
            self.joint_sequence_end = self.motionProxy.getAngles(self.botharms, True)
            print("Hand and joystick is recorded.")
        # Write these joint state into a file (So we could update this in the future-- Calibration)    

        # Reset the state
        # Press another button to Repeat the sequence. 
        if self.headtouch.button is 2 and self.headtouch.state is 1: 
            self.send_movement(self.joint_sequence_start)
            self.send_movement(self.joint_sequence_end)
            print("Moving to stick")

        if self.headtouch.button is 3 and self.headtouch.state is 1: 
            self.send_cartesian_movement()
            self.motionProxy.setAngles("RArm", 1.0, 1.0)
            
        # do the action and grab the stick 
        # lift the stick to starting position, 
        # check the camera to see where the stick is, 
        # if the glob center is where we expected, move on 
        # if it's not then asking for reposition. 

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


    def send_movement(self,position,stay_stiff=True):
        '''send each joint to the robot. Use a non-blocking call to the API
            Input the final position that we want the robot to be in 
            Specify weather or not the robot should stay stiff afterwards.
        '''
        self.motionProxy.setStiffnesses(self.botharms, [1.0 for i in self.botharms])
        fractionMaxSpeed = 0.2
        self.motionProxy.setAngles(self.botharms, position, fractionMaxSpeed)

        if not stay_stiff: 
            self.motionProxy.setStiffnesses(self.botharms, [0.0 for i in self.botharms])

        # print(req, type(req.joint_name), type(req.angle), type(req.speed))

        # if(req.relative):
        #     print("Setting relative position to follow marker")
        #     cur_angle = motionProxy.getAngles(req.joint_name, False)
        #     req.angle = cur_angle[0]*almath.TO_DEG + req.angle
        
        # req = check_limits(req)
        # motionProxy.setAngles(req.joint_name, req.angle*almath.TO_RAD, req.speed)
        # print(motionProxy.getTaskList())
        # time.sleep(3.0)

        #disable = rospy.ServiceProxy('body_stiffness/disable', Empty)
        #disable()
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
