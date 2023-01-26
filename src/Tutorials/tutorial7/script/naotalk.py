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
from naoqi_bridge_msgs.msg import HeadTouch, SetSpeechVocabularyActionGoal,SpeechWithFeedbackActionGoal,WordRecognized
from std_msgs.msg import Bool
from std_srvs.srv import Empty
import math
# from naoqi_bridge_msgs import Blink
# from tutorial7.action.blink import *

# helful nao apps https://github.com/ros-naoqi/nao_robot/tree/master/nao_apps
#  http://docs.ros.org/en/fuerte/api/nao_msgs/html/__BlinkGoal_8py_source.html
#  http://docs.ros.org/en/hydro/api/nao_apps/html/nao__speech_8py_source.html
#  https://github.com/ros-naoqi/nao_robot/blob/master/nao_apps/nodes/nao_speech.py


# head : /tactile_touch button 3 for rear 
#                       button 2 for middle

class nao_talk:
    def __init__(self):
        # self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)
        self.speech_pub = rospy.Publisher("/speech_action/goal", SpeechWithFeedbackActionGoal, queue_size=10)
        self.vocab_pub = rospy.Publisher('/speech_vocabulary_action/goal',SetSpeechVocabularyActionGoal, queue_size=10)
        self.head_sub = rospy.Subscriber("/tactile_touch", HeadTouch, self.headtouch_callback)
        self.word_sub = rospy.Subscriber("/word_recognized", WordRecognized, self.wordrecognized_callback)
        self.head = HeadTouch(0,0)
        self.is_speech_recognition = False
        vocab_msg = SetSpeechVocabularyActionGoal()
        vocab_msg.goal_id.id = "hello"
        vocab_msg.goal.words = ["Hello", "my","friends"]
        self.vocabulary=vocab_msg.goal.words
        self.vocab_pub.publish(vocab_msg)
        self.sentence = []
        print("Vocabulary")

    def headtouch_callback(self, headtouch):
        self.head = headtouch
    def wordrecognized_callback(self, words):
        self.sentence.append(words.words[0])

    def start_talk(self):
        starttalk_service = rospy.ServiceProxy("/start_recognition", Empty)
        starttalk_service()

    def stop_talk(self):
        stoptalk_service = rospy.ServiceProxy("/stop_recognition", Empty)
        stoptalk_service()
    


    ## Repeat the memorized vocabulary as a sentence
    def talk(self):
        sentence = SpeechWithFeedbackActionGoal()
        sentence.goal_id.id = "1"
        for word in self.sentence:
            print(word)
            sentence.goal.say += " "+ word #string with the speech text
        print(sentence)    
        self.speech_pub.publish(sentence)



    def run(self):
        if self.head.button is 1 and self.head.state is 1:
            print("'Start speech recognition")
            self.start_talk()
            # self.is_speech_recognition = True

        if self.head.button is 2 and self.head.state is 1:
            print("Stop recognition")
            self.stop_talk()
            # self.is_speech_recognition = False
            self.talk()
            self.sentence = []

def main():
    rospy.init_node('nao_talk', anonymous=True)
    nao_talk_ = nao_talk()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_talk_.run()
        rate.sleep()


if __name__ == '__main__':
	main()
