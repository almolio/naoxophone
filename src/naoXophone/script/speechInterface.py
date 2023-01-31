#!/usr/bin/env python

import rospy
import sys
import numpy as np
import argparse
from sensor_msgs.msg import JointState
import os 
from naoqi import ALProxy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time
import motion
import almath
import cv2
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


naoIP = str(os.getenv("NAO_IP"))
PORT = 9559

class speechInterface:
    def __init__(self):
        #Text to be said by NAO
        self.speech_pub = rospy.Publisher("/speech_action/goal", SpeechWithFeedbackActionGoal, queue_size=50)
        #Words recognized by NAO
        self.vocab_pub = rospy.Publisher('/speech_vocabulary_action/goal',SetSpeechVocabularyActionGoal, queue_size=50)

        #Head buttons state. 
        self.head_sub = rospy.Subscriber("/tactile_touch", HeadTouch, self.headtouch_callback)
        # self.word_sub = rospy.Subscriber("/word_recognized", WordRecognized, self.wordrecognized_callback)
        """
        self.head.button = 1,2,3
        self.head.state = 0,1 
        """
        self.head = HeadTouch(0,0)
        self.isWaiting = True
        self.listSongs = False


    def headtouch_callback(self, headtouch):
        self.head = headtouch

    def talk(self,message, goal_id):
        sentence = SpeechWithFeedbackActionGoal()
        sentence.goal_id.id = goal_id
        sentence.goal.say = message
        print(sentence)    
        self.speech_pub.publish(sentence)

    def idle_state(self):
        message = ("Hello, what do you wanna do? Press 1 for playing a song and 2 for listening")
        goal_id = "ask_action"
        self.talk(message,goal_id)
        self.isWaiting = False

    def run(self):
        while(self.isWaiting):
            time.sleep(2)
            self.idle_state()
    
        if self.head.button is 1 and self.head.state is 1 and not self.isWaiting:

            message = "Play a song for me"
            goal_id = "play"
            self.talk(message,goal_id)
            """
            START VISUAL RECOGNITION 

            PLAY MEMORIZED SONG

            """
            self.isWaiting = True
        elif self.head.button is 2 and self.head.state is 1 and not self.isWaiting:
            song_1 = "Press button 1 for happy birthday song"
            self.listSongs = True
            #song_2
            #song_3
            self.talk(song_1,"song1")
            # self.talk(song_2)
            # self.talk(song_3)
            while(self.listSongs):
                if self.head.button is 1 and self.head.state is 1:
                    print("Song 1 selected")
                    """
                    FETCH AND PLAY SONG 1
                    """
                    self.isWaiting = True
                    self.listSongs = False
                elif self.head.button is 2 and self.head.state is 1:
                    print("Song 2 selected")
                    """
                    FETCH AND PLAY SONG 1
                    """
                    self.isWaiting = True
                    self.listSongs = False
                elif self.head.button is 3 and self.head.state is 1:
                    print("Song 3 seleted")
                    """
                    FETCH AND PLAY SONG 1
                    """
                    self.isWaiting = True #Go back to idle
                    


def main():
    rospy.init_node('speechInterface', anonymous=True)
    nao_talk = speechInterface()
    rate = rospy.Rate(5)
    # try:
    #     rospy.spin()
    # except KeyboardInterrupt:
    #     print("Shutting down")
    # cv2.destroyAllWindows()
    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_talk.run()
        rate.sleep()


if __name__ == '__main__':
	main()
