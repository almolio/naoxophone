#!/usr/bin/env python

import rospy
import numpy as np
import os 
from naoqi import ALProxy
from cv_bridge import CvBridge, CvBridgeError
import time
from naoqi_bridge_msgs.msg import Bumper
from naoqi_bridge_msgs.msg import BlinkActionGoal
from actionlib_msgs.msg import GoalID

from naoqi_bridge_msgs.msg import HeadTouch, SetSpeechVocabularyActionGoal,SpeechWithFeedbackActionGoal,WordRecognized
from pathlib import Path
import os
from std_srvs.srv import *
from naoXophone.srv import songName

naoIP = str(os.getenv("NAO_IP"))
PORT = 9559
cwd = Path.cwd()
songPath = Path('/home/hrsb/MSNE_HRS/catkin_ws/src/naoXophone/script/songs')

class speechInterface:
    def __init__(self):
        self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.postureProxy = ALProxy('ALRobotPosture', naoIP, PORT)
        #Text to be said by NAO
        self.speech_pub = rospy.Publisher("/speech_action/goal", SpeechWithFeedbackActionGoal, queue_size=50)
        #Words recognized by NAO
        self.vocab_pub = rospy.Publisher('/speech_vocabulary_action/goal',SetSpeechVocabularyActionGoal, queue_size=50)
        #Head buttons state. 
        self.head_sub = rospy.Subscriber("/tactile_touch", HeadTouch, self.headtouch_callback)
        # self.word_sub = rospy.Subscriber("/word_recognized", WordRecognized, self.wordrecognized_callback)
        self.grabsticks = rospy.ServiceProxy("grabSticks", Empty)
        self.playSong = rospy.ServiceProxy("playSong", songName)
        self.learnSong = rospy.ServiceProxy("learnSong", Empty)
        """
        self.head.button = 1,2,3
        self.head.state = 0,1 
        """
        self.head = HeadTouch(0,0)
        self.isWaiting = True
        self.listSongs = False
        self.currentSong = 0
        self.list_all_song()


    def headtouch_callback(self, headtouch):
        self.head = headtouch

    def talk(self,message, goal_id):
        sentence = SpeechWithFeedbackActionGoal()
        sentence.goal_id.id = goal_id
        sentence.goal.say = message
        print(sentence)    
        self.speech_pub.publish(sentence)

    def idle_state(self):
        message = ("Hello, I'm nao xo phone, what can I do? \
                        Press 1 to teach me a new song, \
                        press 2 to browse my song list, \
                        press 3 to play selected song")
        goal_id = "ask_action"
        self.talk(message,goal_id)
        self.isWaiting = False

    def list_all_song(self):
        '''Search directory and list all song '''

        song_list = []
        for entry in songPath.iterdir():
            if entry.is_file():
                _, tail = os.path.split(str(entry))
                song_name = os.path.splitext(tail)[0]
                song_list.append(song_name)

        self.song_list = song_list

    def run(self):
        while(self.isWaiting):
            time.sleep(2)
            self.idle_state()

        self.list_all_song()

        self.total_song = len(self.song_list)  # TODO: Read how many files in songs folder 

        if self.head.button is 1 and self.head.state is 1 and not self.isWaiting:

            message = "You think you can teach me something new. Let me see what you got"
            goal_id = "record"
            self.talk(message,goal_id)
            """
            START VISUAL RECOGNITION 
            # TODO: 

            """
            self.postureProxy.goToPosture("Crouch", 0.5)
            time.sleep(2)
            self.learnSong()


            message = "Impressive, I think I got it."
            self.talk(message,"impressive")    
            
            self.isWaiting = True

        if self.head.button is 2 and self.head.state is 1 and not self.isWaiting:
            print("Button 2 is pressed")
            

            if self.currentSong > (self.total_song-1): 
                self.currentSong = 0
    
            message = "The current song is {}, press 3 to play".format(str(self.song_list[self.currentSong]))
            
            self.talk(message, "song")

            self.currentSong += 1 

        if self.head.button is 3 and self.head.state is 1 and not self.isWaiting: 
            '''Excute Song'''
            # TODO: play the song selected 
            # Grab the stick 
            # and play the song? 
            print("finished grabing the stick")
            # self.motionProxy.rest()
            # Call play song service passing it the song name, return empty 
            self.playSong(str(self.song_list[self.currentSong]))


def main():
    rospy.init_node('speechInterface', anonymous=True)
    nao_talk = speechInterface()
    rate = rospy.Rate(5)

    time.sleep(5)

    nao_talk.grabstick()
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
