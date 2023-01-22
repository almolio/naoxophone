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
# from naoqi_bridge_msgs import Blink
# from tutorial7.action.blink import *

# helful nao apps https://github.com/ros-naoqi/nao_robot/tree/master/nao_apps
#  http://docs.ros.org/en/fuerte/api/nao_msgs/html/__BlinkGoal_8py_source.html




class nao_blink:
    def __init__(self):
        # self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)
        self.bumper_sub = rospy.Subscriber("/bumper", Bumper, self.bumper_callback)
        self.blink_pub = rospy.Publisher('/blink/goal',BlinkActionGoal, queue_size=10)
        self.cancel_pub = rospy.Publisher('/blink/cancel',GoalID, queue_size=10)
        self.bump = None

    def bumper_callback(self, bump):
        self.bump = bump
        print(bump)

    def run(self):
        # check the bump
        if self.bump is not None:
            if self.bump.state == 1: 
                if self.bump.bumper is 0: 
                    print("the right foot is pressed")
                    green = ColorRGBA()
                    green.r = 0
                    green.g = 1
                    green.b = 0
                    green.a = 1
                    blink_msg = BlinkActionGoal()
                    blink_msg.goal_id.id = "BlinkGRUENE"
                    blink_msg.goal.colors = [green]
                    blink_msg.goal.blink_duration = Duration(4)
                    blink_msg.goal.blink_rate_mean = 0.5
                    blink_msg.goal.blink_rate_sd = 1
                    cancel_msg = GoalID()
                    cancel_msg.id=blink_msg.goal_id.id
                    self.blink_pub.publish(blink_msg)
                    time.sleep(4)
                    self.cancel_pub.publish(cancel_msg)
                    
                if self.bump.bumper is 1: 
                    print("the left foot is pressed")
                    blink_msg = BlinkActionGoal()
                    blink_msg.goal_id.id = "BlinkROT"
                    blink_msg.goal.colors = [ColorRGBA(1,0,0,1)]
                    blink_msg.goal.blink_duration = Duration(2)
                    blink_msg.goal.blink_rate_mean = 0.5
                    blink_msg.goal.blink_rate_sd = 1
                    cancel_msg = GoalID()
                    cancel_msg.id=blink_msg.goal_id.id
                    self.blink_pub.publish(blink_msg)
                    time.sleep(2)
                    self.cancel_pub.publish(cancel_msg)
                

                #self.cancel_pub.publish(cancel_msg)



def main():
    rospy.init_node('nao_blink', anonymous=True)
    nao_blink_ = nao_blink()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_blink_.run()
        rate.sleep()


if __name__ == '__main__':
	main()
