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

naoIP = str(os.getenv("NAO_IP"))
PORT = 9559
cwd = Path.cwd()
songPath = cwd / "songs"

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
        self.currentSong = 0

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
                        2 browse my song list, \
                        3 to play")
        goal_id = "ask_action"
        self.talk(message,goal_id)
        self.isWaiting = False

    def list_all_song(self):
        '''Search directory and list all song '''

        song_list = []
        for entry in songPath.iterdir():
            if entry.is_file():
                song = os.path.splitext(str(entry))[0]
                song_list.append(song)

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
            # TODO: Add the script to run the song recording 
            PLAY MEMORIZED SONG

            """
            self.isWaiting = True

            message = "Impressive, I think I got it."

        if self.head.button is 2 and self.head.state is 1 and not self.isWaiting:
            self.currentSong += 1 

            if self.currentSong > self.total_song: 
                self.currentSong = 0
    
            message = "The current song is song number{}".format(str(self.song_list[self.currentSong]))
            self.talk(message, "song")

        if self.head.button is 3 and self.head.state is 1 and not self.isWaiting: 
            '''Excute Song'''
            # TODO: play the song selected 
            # Grab the stick 
            # and play the song? 
            
            ## Approach 1 call grab stick service or broadcast 



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
