#!/usr/bin/env python2

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
        self.head_sub = rospy.Subscribe("/tactile_touch", HeadTouch, self.headtouch_callback)
        self.bump = None
        self.foot_contact = True
        self.head = None
        self.is_walking = False
        

    # def bumper_callback(self, bump):
    #     self.bump = bump
    #     print(bump)

    def footcontact_callback(self, is_contact):
        self.foot_contact = is_contact

    def headtouch_callback(self, headtouch):
        self.head = headtouch

    def stop_walk(self):
        stopwalk_service = rospy.ServiceProxy("/stop_walk_srv")
        stopwalk_service()

    def run(self):
        if self.head.buttom is 3 and self.head.state is 1:
            self.is_walking = not self.is_walking
            
        if self.is_walking == False:
            self.stop_walk()
        else:
            go_forward = Pose2D(10,0,0)
            self.walk_pub(go_forward)

def main():
    rospy.init_node('nao_walk', anonymous=True)
    nao_walk = nao_walk()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_walk.run()
        rate.sleep()


if __name__ == '__main__':
	main()
