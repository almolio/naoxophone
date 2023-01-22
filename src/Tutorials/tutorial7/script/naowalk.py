#!/usr/bin/env python

import rospy
import sys
import cv2
from std_msgs.msg import String
import motion
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 
from pathlib import Path
import matplotlib.pyplot as plt
import tf
import time
# naoqi_bridge_msgs/Bumper
import actionlib
from naoqi_bridge_msgs.msg import Bumper
from naoqi_bridge_msgs.msg import BlinkActionGoal
from actionlib_msgs.msg import GoalID
from std_msgs.msg import ColorRGBA
from genpy import Duration

from geometry_msgs.msg import Pose2D
from naoqi_bridge_msgs.msg import HeadTouch
from std_msgs.msg import Bool
from std_srvs.srv import Empty
import math
# from naoqi_bridge_msgs import Blink
# from tutorial7.action.blink import *

# helful nao apps https://github.com/ros-naoqi/nao_robot/tree/master/nao_apps
#  http://docs.ros.org/en/fuerte/api/nao_msgs/html/__BlinkGoal_8py_source.html


# head : /tactile_touch button 3 for rear 

class nao_walk:
    def __init__(self):
        # self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)
        self.footcontact_sub = rospy.Subscriber("/foot_contact", Bool, self.footcontact_callback)
        self.walk_pub = rospy.Publisher('/cmd_pose',Pose2D, queue_size=10)
        self.head_sub = rospy.Subscriber("/tactile_touch", HeadTouch, self.headtouch_callback)
        self.bump = None
        self.foot_contact = True
        self.head = HeadTouch(0,0)
        self.is_walking = False


    def footcontact_callback(self, is_contact):
        self.foot_contact = is_contact

    def headtouch_callback(self, headtouch):
        self.head = headtouch

    def stop_walk(self):
        stopwalk_service = rospy.ServiceProxy("/stop_walk_srv", Empty)
        stopwalk_service()

    def run(self):
        if self.head.button is 3 and self.head.state is 1:
            self.is_walking = not self.is_walking
            # print("Walking Status {}".format(self.is_walking))

        if self.foot_contact == False: 
            self.is_walking = False

        if self.is_walking == False:
            # print("Stop Walking")
            self.stop_walk()
        else:
            print("Start Walking")
            go_forward = Pose2D(2,0,0)
            # go_left = Pose2D(4, 0, math.pi)
            turn_left = Pose2D(0, 0, math.pi/2)
            turn_right = Pose2D(0,0, -math.pi/2)
            self.walk_pub.publish(turn_left)
            # time.sleep(1)
            self.walk_pub.publish(go_forward)
            # time.sleep(1)
            self.walk_pub.publish(turn_right)
            # time.sleep(1)
            # self.rate.sleep()
            

def main():
    rospy.init_node('nao_walk', anonymous=True)
    nao_walk_ = nao_walk()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_walk_.run()
        rate.sleep()


if __name__ == '__main__':
	main()
