#!/usr/bin/env python2
# -*- encoding: UTF-8 -*-
import rospy
import time
import almath
import sys
from naoqi import ALProxy
from nao_control_tutorial_1.srv import jointAngle, jointAngleResponse, timedInterpolation,  timedInterpolationResponse
# motionProxy =0
import argparse
import math
import numpy as np
# from tutorial_4_opticalflow import arucodetection  

coor_in_strings_global = ''


def jointAngle_client(name, angle, speed):
    #HeadYaw, HeadPitch, LShoulderRoll, LShoulderPitch, 
    rospy.wait_for_service('jointAngle')
    try:
        print('Starting Client.')
        move        = rospy.ServiceProxy('jointAngle', jointAngle)
        print('Starting Response.')
        response    = move(name, angle, speed)
        #print(response)
        return response.angle
    except rospy.ServiceException as e:
        print('Service call failed: %s'%e)


def timedInterpolation_client(names, angleLists, times):
    #HeadYaw, HeadPitch, LShoulderRoll, LShoulderPitch, 
    rospy.wait_for_service('timedInterpolation')
    try:
        print('Starting Client.')
        move        = rospy.ServiceProxy('timedInterpolation', timedInterpolation)
        print('Starting Response.')
        response    = move(names, angleLists, times)
        #print(response)
        return response.angle
    except rospy.ServiceException as e:
        print('Service call failed: %s'%e)



def reactive_headtrack(x, y):
    # Safety limit in rad
    # PITCH: -0.67  TO 0.5
    # YAW: -2.08 TO 2.07         
    r = rospy.Rate(4)  # Hz 
    motionProxy = ALProxy('ALMotion','10.152.246.81', 9559)
    # names    = ["HeadYaw", "HeadPitch"]
    names = ["HeadYaw"]
    # This is in Pixel
    # x_max 320, y_max = 240
    x_middle = 160
    y_middle = 120
    
    x_angle_current = motionProxy.getAngles(names[0], True)
    r.sleep()
    print('current angle Yall {}'.format(x_angle_current))
    x_angle_current = x_angle_current[0]
    y_angle_current = motionProxy.getAngles(names[0], True)  # change back to idx 0 for run with headpitch
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


def return_head_to_neutral(): 
    names    = ["HeadYaw", "HeadPitch"]
    angleLists = [0.0, 0.0]
    timeLists  = [1.2, 1.8]
    # timedInterpolation_client(names[0], str(angleLists[0]), str(timeLists[0]))
    timedInterpolation_client(l_2_str(names), l_2_str(angleLists), l_2_str(timeLists))

def l_2_str(list):
    return '{} {}'.format(list[0],list[1])

def usage():
    return '%s [name angle speed]'%sys.argv[0]


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


if __name__ == '__main__':
    # if len(sys.argv) == 5: #call the client with mode normal joint control or interpolation as the first arg
    if(str(sys.argv[1])=="normal"):
        name  = str(sys.argv[2])
        angle = float(sys.argv[3])
        speed = float(sys.argv[4])
        print('Normal: Requesting name {} angle {} and speed {}'.format(name, angle, speed))
        print('Current angle is {}'.format(jointAngle_client(name, angle, speed)))
    elif(str(sys.argv[1])=="interpolation"):
        ###### DEGREE ARE IN RAD ################
        # rosrun nao_control_tutorial_1 move_client.py 'interpolation' 'HeadYaw' 1.0 -1.0 1.0 1.0 10.0 20.0
        names       = str(sys.argv[2])
        angleLists  = str(str(sys.argv[3])+' '+str(sys.argv[4])+' '+str(sys.argv[5]))
        times       = str(str(sys.argv[6])+' '+str(sys.argv[7])+' '+str(sys.argv[8]))
        print('Interpolation: Requesting name {} angles {} and times {}'.format(names, angleLists, times))
        print('Current angle is {}'.format(timedInterpolation_client(names, angleLists, times)))
    elif(str(sys.argv[1])=="Shoulder"):
        # names       = str(sys.argv[2])
        # angleLists  = str(str(sys.argv[3])+' '+str(sys.argv[4])+' '+str(sys.argv[5]))
        # times       = str(str(sys.argv[6])+' '+str(sys.argv[7])+' '+str(sys.argv[8]))
        # print('Interpolation: Requesting name {} angles {} and times {}'.format(names, angleLists, times))
        # print('Current angle is {}'.format(jointAngle_client('RShoulderRoll', 30.0, 0.2)))
        # rospy.sleep(2)
        # print('Current angle is {}'.format(jointAngle_client('RShoulderPitch', 30.0, 0.2)))
        print('Current angle is {}'.format(jointAngle_client('RElbowRoll', 70.0, 0.2)))
        rospy.sleep(2)
        print('Current angle is {}'.format(jointAngle_client('RWristYaw', 30.0, 0.2)))

    elif(str(sys.argv[1])=="Reactive"):
        from std_msgs.msg import String
        rospy.init_node('Reative_moving', anonymous=True)
        rospy.Subscriber('/aruco_coordinate', String, callback_coordinate)
        return_head_to_neutral()
        r = rospy.Rate(4)  # Hz 
        while not rospy.is_shutdown():
            x, y = get_coordinate_from_strings(coor_in_strings_global)
            reactive_headtrack(x, y)
            r.sleep()
        