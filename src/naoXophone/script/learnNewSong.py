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
from naoXophone.srv import *
from naoqi import ALProxy

naoIP = str(os.getenv("NAO_IP"))
PORT = 9559

class learnSong:
    # adapted from https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/
    # pose estimation adapted from https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python/blob/main/pose_estimation.py

    def __init__(self):
        self.bridge     = CvBridge()
        self.image_sub  = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",\
                                        Image,self.callback)

        self.motionProxy = ALProxy('ALMotion',naoIP, PORT) 
        
        self.played_tones = []
        self.rate = rospy.Rate(5)

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

        print("Calibration Done")
        
    def recordSong(self):
        tones = find_played_tones(self.raw_img, top_bound = 100, \
            bottom_bound=200, ranges_bottom = self.ranges_bottom, ranges_top = self.ranges_top)
        self.played_tones = np.append(self.played_tones, tones )
        
        # image = np.copy(self.raw_img)
        # image[:,:,0] = mask*200
        # cv2.imshow("mask", self.raw_img)

    def moveToRecordingPose(self):
        
        joint_names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
                        "LHand", "LHipYawPitch", "LHipRoll", "LHipPitch", "LKneePitch", "LAnklePitch", "LAnkleRoll", "RHipYawPitch",
                        "RHipRoll", "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll", "RShoulderPitch", "RShoulderRoll",
                        "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
        angle_list = [0.013764142990112305, 0.01683211326599121, 1.745650053024292, 0.07052206993103027, -1.2303099632263184, -0.17943596839904785, -1.0032777786254883, 0.23559999465942383, -0.23926210403442383, -0.09813404083251953, -0.7899680137634277, 2.112546443939209, -1.1894419193267822, 0.07501578330993652, -0.23926210403442383, 0.0844118595123291, -0.7961878776550293, 2.112546443939209, -1.186300277709961, -0.07586973160505295, 1.5585861206054688, -0.05373191833496094, 0.3359041213989258, 0.04606199264526367, 1.64900803565979, 0.7943999767303467]
        speed = 0.5
        self.motionProxy.setAngles(joint_names, angle_list, speed)
        print("move to recording pose")

    def service_handle(self,req):
        print("service is called")
        # name  = sys.argv[1]
        name = req

        dur = 40

        # while not rospy.is_shutdown(): 
            # print(time.time()-start)

        self.moveToRecordingPose()
    
        # if 5 <= (time.time()-start) <= 6:

        print('Start Callibrating ...')
        self.callibrate()

        start = time.time()
        while (time.time()-start) <= dur:

            print('Start Recording ...')
            # print('looping after run')
            self.recordSong()
            self.rate.sleep()

        # if dur <=(time.time()-start) <= dur+1:
        print('End Recording ...')
        #save song

        tones = ['red', 'orange', 'yellow', 'green', 'blue', 'white', 'lila', 'red', 'none']
        times_in_frames, tones_in_int = clean_up(self.played_tones)

        print('times: ', times_in_frames.astype(int))
        print('tones: ', tones_in_int.astype(int))

        save_path = '/home/hrsb/MSNE_HRS/catkin_ws/src/naoXophone/script/songs'

        # Horiontal stack and tranpose
        song_to_save = np.vstack(tones_in_int,times_in_frames).T

        # np.save(os.path.join(save_path, '{}_times_fps.npy'.format(name)), times_in_frames)
        # np.save(os.path.join(save_path, '{}_tones_int.npy'.format(name)), tones_in_int)
        np.save(os.path.join(save_path, '{}.npy'.format(name)), song_to_save)

        return []

def main ():
    print("SERVICE INIT")
    # TODO: add service so that we can pass a song name before calling service 
    rospy.init_node('learnSong_service', anonymous=True)
    nao_learnSong = learnSong()
    
    s = rospy.Service('learnSong', Empty, nao_learnSong.service_handle)
    rospy.spin() 


if __name__ == '__main__':
	main()