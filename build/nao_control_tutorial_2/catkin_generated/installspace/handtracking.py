#!/usr/bin/env python2
# -*- encoding: UTF-8 -*-

import rospy
import almath
from naoqi import ALProxy
# from nao_control_tutorial_1.srv import jointAngle, jointAngleResponse, timedInterpolation,  timedInterpolationResponse
from nao_control_tutorial_2.srv import MoveJoints, MoveJointsResponse
import tf
import numpy as np
import motion 
import math

naoIP = '10.152.246.59' #81

class autohandtrack():
    def __init__(self):
        self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)
        self.tflistener = tf.TransformListener()


# GET THE TRANSFORMATION MATRIX FROM ARUCO TO CAMERA
    def get_transform(self):

        print("getting tranformation mat")
        # H_aruco_to_torso = np.identity(4)
        try: 
            (trans,rot) = self.tflistener.lookupTransform("/CameraBottom_frame","/ARUCOFRAME",rospy.Time(0))
            # print("aruco thingy")
            # print(trans,rot)
            H_aruco_to_opticalcamera = tf.transformations.euler_matrix(rot[0],rot[1],rot[2])
            # tf.transformations.translation_from_matrix 
            H_aruco_to_opticalcamera[:3,3] = trans #np.transpose(trans)
   
            useSensorValues = True
            # H_opticalcamera_to_camera = tf.transformations.euler_matrix(-math.pi/2,0,-math.pi/2)

            # H_aruco_to_camera  = np.multiply(H_aruco_to_opticalcamera, H_opticalcamera_to_camera)
            H_aruco_to_camera = H_aruco_to_opticalcamera
            print("H_aruco_to_camera \n {}".format(H_aruco_to_camera))

            
            H_camera_to_torso = self.motionProxy.getTransform("CameraBottom",
                                motion.FRAME_TORSO, useSensorValues)
            H_camera_to_torso = np.asarray(H_camera_to_torso).reshape([4,4])
            print("H_camera_to_torso \n {}".format(H_camera_to_torso))           
            
            H_aruco_to_torso = np.multiply(H_camera_to_torso, H_aruco_to_camera)
            print("H_aruco_to_torso \n {}".format(H_aruco_to_torso))
            return H_aruco_to_torso   
        except tf.LookupException: 
            pass
            return np.identity(4)
 


    def call_move_service(self, joint_name, pose, vel , time):
        #HeadYaw, HeadPitch, LShoulderRoll, LShoulderPitch, 
        
        rospy.wait_for_service('Pose6D')

        #### Define the variable to put in the request 
        # joint_name 
        x_pos = str(pose[0])
        y_pos = str(pose[1])
        z_pos = str(pose[2])
        x_rot = str(pose[3])
        y_rot = str(pose[4])
        z_rot = str(pose[5])
        max_vel = str(vel)
        exe_time = str(time)

        try:
            # print('Starting Client.')
            move        = rospy.ServiceProxy('Pose6D', MoveJoints)
            # print('Starting Response.')
            response    = move(joint_name, x_pos, y_pos, z_pos, 
                                x_rot, y_rot, z_rot, 
                                max_vel, exe_time)
            return response
        except rospy.ServiceException as e:
            print('Service call failed: %s'%e)

    def homogeneous_to_pose(self, homogeneous_mat):
        rvec = tf.transformations.euler_from_matrix(homogeneous_mat)
        tvec = homogeneous_mat[:3,3]
        return np.hstack([tvec, rvec])


    def run(self): 

        transform_mat = self.get_transform()
        print("final transformation matrix {} ".format(transform_mat))
        pose = self.homogeneous_to_pose(transform_mat)
        jointname = "RArm" # "LArm"
        vel = 0.5 
        time = 5.0
        self.call_move_service(joint_name=jointname,
                        pose=pose,
                        vel= vel, 
                        time= time)
        self.rate.sleep()


def main():
    rospy.init_node('auto_hand_tracking', anonymous=True)
    handtrack_routine = autohandtrack()
    # print('started node')
    rate = rospy.Rate(5)

    while not rospy.is_shutdown(): 
        # print('looping after run')
        handtrack_routine.run()
   
        rate.sleep()


if __name__ == '__main__':
	main()
