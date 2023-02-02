#!/usr/bin/env python

import rospy
import sys
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 
from pathlib import Path
import matplotlib.pyplot as plt
from visual_detection import callibration, find_played_tones, clean_up
import time
import os
import sys
from std_srvs.srv import *
from naoXophone.srv import songName


class learnSong:
    # adapted from https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/
    # pose estimation adapted from https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python/blob/main/pose_estimation.py

    def __init__(self):
        self.bridge     = CvBridge()
        self.image_sub  = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",\
                                        Image,self.callback)

        
        self.played_tones = []

    def callback (self, image):
        try: # if there is an image
            self.raw_img = self.bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")
        except CvBridgeError as e:
            print (e)
        image_hsv   = cv2.cvtColor(self.raw_img, cv2.COLOR_BGR2HSV)
        #cv2.imshow("Bottom Camera", self.raw_img)
        cv2.imshow("hsv Camera", image_hsv)

        cv2.waitKey(5) 

    def callibrate(self):

        self.dil_red, self.ranges_bottom, self.ranges_top = callibration(self.raw_img, top_bound = 100, \
            bottom_bound=200)
        
    def recordSong(self):
        tones = find_played_tones(self.raw_img, top_bound = 100, \
            bottom_bound=200, ranges_bottom = self.ranges_bottom, ranges_top = self.ranges_top)
        self.played_tones = np.append(self.played_tones, tones )
        
        # image = np.copy(self.raw_img)
        # image[:,:,0] = mask*200
        # cv2.imshow("mask", self.raw_img)
       

def run(req):
    start = time.time()
    # name  = sys.argv[1]
    name = req # TODO: add service to pass name 

    nao_learnSong = learnSong()
    rate = rospy.Rate(5)
    dur = 40

    # while not rospy.is_shutdown(): 
        # print(time.time()-start)

    if 5 <= (time.time()-start) <= 6:

        print('Start Callibrating ...')
        nao_learnSong.callibrate()

    while (time.time()-start) <= dur and (time.time()-start) >= 6:

        print('Start Recording ...')
        # print('looping after run')
        nao_learnSong.recordSong()
        rate.sleep()

    if dur <=(time.time()-start) <= dur+1:
        print('End Recording ...')
        #save song

        tones = ['red', 'orange', 'yellow', 'green', 'blue', 'white', 'lila', 'red', 'none']
        times_in_frames, tones_in_int = clean_up(nao_learnSong.played_tones)

        print('times: ', times_in_frames.astype(int))
        print('tones: ', tones_in_int.astype(int))

        save_path = '/home/hrsb/MSNE_HRS/catkin_ws/src/naoXophone/script/songs'

        # Horiontal stack and tranpose
        song_to_save = np.vstack(tones_in_int,times_in_frames).T

        # np.save(os.path.join(save_path, '{}_times_fps.npy'.format(name)), times_in_frames)
        # np.save(os.path.join(save_path, '{}_tones_int.npy'.format(name)), tones_in_int)
        np.save(os.path.join(save_path, '{}.npy'.format(name)), tones_in_int)
        # break


def main ():

    # TODO: add service so that we can pass a song name before calling service 
    rospy.init_node('learnSong_service', anonymous=True)
    s = rospy.Service('learnSong', Empty, run)
    rospy.spin()


if __name__ == '__main__':
	main(sys.argv)