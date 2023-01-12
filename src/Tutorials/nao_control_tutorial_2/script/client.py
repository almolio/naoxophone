#!/usr/bin/env python
import rospy
import time
import almath
import sys
from naoqi import ALProxy
from nao_control_tutorial_2.srv import MoveJoints, MoveJointsResponse
# motionProxy =0
import argparse
import math
import numpy as np
import tf
# from tutorial_4_opticalflow import arucodetection  

coor_in_strings_global = ''
naoIP = '10.152.246.81'

def pose_client(joint_name,x_pos,y_pos,z_pos,x_rot,y_rot,z_rot,max_vel,exe_time):
    #HeadYaw, HeadPitch, LShoulderRoll, LShoulderPitch, 
    rospy.wait_for_service('Pose6D')
    try:
        print('Starting Client.')
        pose        = rospy.ServiceProxy('Pose6D', MoveJoints)
        print('Starting Response.')
        response    = pose(joint_name,x_pos,y_pos,z_pos,x_rot,y_rot,z_rot,max_vel,exe_time)
        #print(response)
        return response.x_pos, response.y_pos, response.z_pos, response.x_rot, response.y_rot, response.z_rot
    except rospy.ServiceException as e:
        print('Service call failed: %s'%e)
        

def callback_coordinate(coor_in_strings):
    global coor_in_strings_global
    coor_in_strings_global = coor_in_strings.data

def get_coordinate_from_strings (string_input):
    splited = string_input.split()
    if len(splited) == 0: 
        x = 0 
        y = 0 
    else:
        x = int(splited[0])
        y = int(splited[1])
    return x, y



def reactive_arm(x, y,names):
    #Safety limit angles for arm      
    r = rospy.Rate(4)  # Hz 
    motionProxy = ALProxy('ALMotion',naoIP, 9559)
    # names    = ["HeadYaw", "HeadPitch"]
    # This is in Pixel
    # x_max 320, y_max = 240
    x_middle = 160
    y_middle = 120
    
    x_cur,y_cur,z_cur,x_rot_cur,y_rot_cur,z_rot_cur  = motionProxy.getPosition(names, True)
    r.sleep()
    print('current angle pitch {}'.format(y_angle_current))
    y_angle_current = y_angle_current[0]
    x_angle_max = 2.06  # Yaw
    y_angle_max = 0.5    # Pitch
    move_x_to = x_angle_current
    move_y_to = y_angle_current

    # magn     = np.abs([x, y] - [x_middle, y_middle])

    x_dist   = x - x_middle
    y_dist   = y - y_middle

    print('x y distance to middle {}  {}'.format(x_dist, y_dist))
    
    increment = 0.07
    # if above the threshold then we can calculate
    if abs(x_dist) > 5 and abs(y_dist) > 5: 

        # move x and y to current +/- increments depends of distance    
        if x_dist > 0: 
            move_x_to = x_angle_current - increment
        elif x_dist < 0: 
            move_x_to = x_angle_current + increment

        if y_dist > 0:
            move_y_to = y_angle_current + increment
        elif y_dist < 0:    
            move_y_to = y_angle_current - increment
    # if x_angle_current <= x_angle_max:
    #     x_angle_abs =  -x_angle_max - x_angle_current 
    # else:
    #     x_angle_abs =   x_angle_max - x_angle_current

    # if y_angle_current <= x_angle_max:
    #     y_angle_abs = - y_angle_max - y_angle_current 
    # else:
    #     y_angle_abs =   y_angle_max - y_angle_current

    # x_fraction_dist = np.abs(x_dist)/x_middle
    # y_fraction_dist = np.abs(y_dist)/y_middle
    
    # print('Fractional distance {}  {}'.format(x_fraction_dist,y_fraction_dist))
    # x_angle  = 0.8 * x_fraction_dist * x_angle_abs
    # y_angle  = 0.8 * y_fraction_dist * y_angle_abs
    # angleLists = [x_angle*almath.TO_RAD, y_angle*almath.TO_RAD]
    # angleLists = [move_x_to, move_y_to]
    timeLists  = [0.5]
    angleLists = [move_x_to]

    print('Angle should move to here {} '.format((angleLists)))

    # timedInterpolation_client("HeadYaw", l_2_str(angleLists), l_2_str(timeLists))
    timedInterpolation_client("HeadYaw", str(angleLists[0]), str(timeLists[0])) 


if __name__ == '__main__':
    # if len(sys.argv) == 5: #call the client with mode normal joint control or interpolation as the first arg
    joint_name = str(sys.argv[1])
    x_pos= str(sys.argv[2])
    y_pos= str(sys.argv[3])
    z_pos= str(sys.argv[4])
    x_rot= str(sys.argv[5])
    y_rot= str(sys.argv[6])
    z_rot= str(sys.argv[7])
    max_vel= str(sys.argv[8])
    exe_time= str(sys.argv[9])
    print('Normal: Requesting ', joint_name,x_pos,y_pos,z_pos,x_rot,y_rot,z_rot,max_vel,exe_time)
    print('Current response {}'.format(pose_client(joint_name,x_pos,y_pos,z_pos,x_rot,y_rot,z_rot,max_vel,exe_time)))
    
    # from std_msgs.msg import String
    # rospy.init_node('Reative_moving', anonymous=True)
    # rospy.Subscriber('/aruco_coordinate', String, callback_coordinate)
    # r = rospy.Rate(4)  # Hz 
    # while not rospy.is_shutdown():
    #     x, y = get_coordinate_from_strings(coor_in_strings_global)
    #     reactive_headtrack(x, y)
    #     r.sleep()
    
    
    # rospy.init_node('pose_client', anonymous=True)
    # r = rospy.Rate(4)  # Hz 
    # while not rospy.is_shutdown():
    #     print('Normal: Requesting ', joint_name,x_pos,y_pos,z_pos,x_rot,y_rot,z_rot,max_vel,exe_time)
    #     print('Current response {}'.format(pose_client(joint_name,x_pos,y_pos,z_pos,x_rot,y_rot,z_rot,max_vel,exe_time)))
    #     r.sleep()