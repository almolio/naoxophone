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


# docs: http://doc.aldebaran.com/2-4/naoqi/motion/control-joint-api.html 
# http://doc.aldebaran.com/2-8/family/nao_technical/masses_naov6.html
"""
#LArm angle limits in  degrees and radians
LShoulderPitch 	Left shoulder joint front and back (Y) 	-119.5 to 119.5 	-2.0857 to 2.0857
LShoulderRoll 	Left shoulder joint right and left (Z) 	-18 to 76 	        -0.3142 to 1.3265
LElbowYaw   	Left shoulder joint twist (X) 	        -119.5 to 119.5 	-2.0857 to 2.0857
LElbowRoll 	    Left elbow joint (Z)            	    -88.5 to -2 	    -1.5446 to -0.0349
LWristYaw 	    Left wrist joint (X) 	                -104.5 to 104.5 	-1.8238 to 1.8238
LHand 	        Left hand 	                            Open and Close 	       Open and Close

"""

naoIP = str(os.getenv("NAO_IP"))
PORT = 9559

class notePositions:
    def __init__(self):
        self.motionProxy = ALProxy('ALMotion',naoIP, PORT) 
        self.rate = rospy.Rate(2)
        self.postureProxy = ALProxy('ALRobotPosture', naoIP, PORT)
        L_Arm_joint_limits=self.motionProxy.getLimits("LArm")
        R_Arm_join_limits = self.motionProxy.getLimits("RArm")
        self.fractionMaxSpeed = 0.8
        self.notePosition1 = [5*almath.TO_RAD, 0.425580539703369, -1.488802108764648, -0.4662940502166748, 1.253660583496094]
        self.notePosition2 = [5*almath.TO_RAD, 0.3210121536254883, -1.48802108764648, -0.4662940502166748, 1.253660583496094]
        self.notePosition3 = [5*almath.TO_RAD, 0.2421559715270996, -1.48802108764648, -0.4662940502166748, 1.253660583496094]
        self.notePosition4 = [5*almath.TO_RAD, 0.1368161201477051, -1.48802108764648, -0.4662940502166748, 1.253660583496094]
        self.notePosition5 = [5*almath.TO_RAD, -0.2423560428619385, 1.483336091041565, 0.357464075088501, -1.3683700561523438]
        self.notePosition6 = [5*almath.TO_RAD, -0.36058002471923828, 1.483336091041565, 0.357464075088501, -1.3683700561523438]
        self.notePosition7 = [5*almath.TO_RAD, -0.458002471923828, 1.483336091041565, 0.357464075088501, -1.3683700561523438]
        self.notePosition8 = [5*almath.TO_RAD, -0.52958002471923828, 1.483336091041565, 0.357464075088501, -1.3683700561523438]
        self.song_1=np.zeros([25,2])
        self.song_1[:,0] = [1, 1, 2, 1, 4, 3, 1, 1, 2, 1,5,4, 1, 1, 8, 6, 4, 3, 2, 7, 7, 6, 4, 5, 4] #Happy Birthday
        self.song_1[:,1] = [0.5, 0.5, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 2]
        self.scale=np.zeros([8,2])
        self.scale[:,0]=[1,2,3,4,5,6,7,8]
        self.scale[:,1]=[1,1,1,1,1,1,1,1]
        self.song_list=["Happy Birthday"]
        #self.motionProxy.rest()
        # self.motionProxy.setStiffnesses("Body",1.0)
        # time.sleep(2)
        #self.postureProxy.goToPosture("Crouch", 0.5)
        #time.sleep(5)
        #self.motionProxy.setAngles(["LHipPitch", "RHipPitch"], [-0.8, -0.8], self.fractionMaxSpeed)
        # self.motionProxy.setStiffnesses("LArm",0.0) #Disable stiffness in the arm
        # self.motionProxy.setStiffnesses("RArm",0.0) #Disable stiffness in the arm

        #self.grabStick()
        # self.motionProxy.setStiffnesses("LArm", 1.0) #Enable stiffness in the arm
        # time.sleep(2)   
        
        # Subscribe to the camera 
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback_img)


    def grabStick(self):
        self.motionProxy.setStiffnesses("RHand", 1.0)
        self.motionProxy.setStiffnesses("LHand", 1.0)
        self.motionProxy.setAngles("LHand", 1.0, 1.0)
        self.motionProxy.setAngles("RHand", 1.0, 1.0)
        time.sleep(2)
        self.motionProxy.setStiffnesses("RHand", 1.0)
        self.motionProxy.setStiffnesses("LHand", 1.0)
        self.motionProxy.setAngles("LHand", 0.0, 1.0)
        self.motionProxy.setAngles("RHand", 0.0, 1.0)

        
    def callback_img(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.imshow("Bottom Camera", cv_image)
        cv2.waitKey(3)


    def recordArmAngles(self,chainName):
        """
        Records the angle of each joint
        """
        names=chainName
        if chainName == "LArm":
            names = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
        elif chainName == "RArm":
            names = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
        useSensorValues = True
        arm_angles = self.motionProxy.getAngles(names,useSensorValues)
        return arm_angles

    def hitNote(self,note):
        """
        Position the arm above the note and turn wrist and shoulder to hit the note
        chainName: LArm or RArm
        notePosition: init position for the note
        """
        if note==1:
            names = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
            notePosition=self.notePosition1
        elif note == 2:
            names = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
            notePosition=self.notePosition2
        elif note == 3:
            names = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
            notePosition=self.notePosition3
        elif note == 4:
            names = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
            notePosition=self.notePosition4
        elif note == 5:
            names = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
            notePosition=self.notePosition5
        elif note == 6:
            names = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
            notePosition=self.notePosition6
        elif note == 7:
            names = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
            notePosition=self.notePosition7
        elif note == 8:
            names = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
            notePosition=self.notePosition8

        self.motionProxy.angleInterpolationWithSpeed(names, notePosition, self.fractionMaxSpeed)

        ## Move arm to position above note
        # self.motionProxy.angleInterpolation([chainName], frame, notePosition,
        #                             axisMaskList, timeList)


        if note in [1,2,3,4]:
            joints = ["LElbowYaw", "LShoulderPitch"]
            elbow_angle=20.0
            shoulder_angle = 30
        elif note in [5,6,7,8]:
            joints = ["RElbowYaw", "RShoulderPitch"]
            elbow_angle=-20.0
            shoulder_angle = 30
        angleLists  = [[elbow_angle*almath.TO_RAD, 0.0], [shoulder_angle*almath.TO_RAD, 0.0]]
        timeLists   = [[1.0, 2.0], [1.0, 2.0]]
        isAbsolute = False  #angle relative to current position
        self.motionProxy.angleInterpolation(joints, angleLists, timeLists, isAbsolute)



    def turnDown(self,chainName):
        names=[]
        if chainName == "LArm":
            names = ["LElbowYaw", "LShoulderPitch"]
            elbow_angle=20.0
            shoulder_angle = 30
        elif chainName == "RArm":
            names = ["RElbowYaw", "RShoulderPitch"]
            elbow_angle=-20.0
            shoulder_angle = 30

        angleLists  = [[elbow_angle*almath.TO_RAD, 0.0], [shoulder_angle*almath.TO_RAD, 0.0]]
        timeLists   = [[1.0, 2.0], [ 1.0, 2.0]]
        isAbsolute = False  #angle relative to current position
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    

    def playSong(self,song):
        for i in range(len(song[:,0])):
            note = song[i,0]
            self.hitNote(note)
            time.sleep(song[i,1])


    def run(self):
        self.motionProxy.setStiffnesses("LArm",1.0) #Disable stiffness in the arm
        self.motionProxy.setStiffnesses("RArm",1.0) #Disable stiffness in the arm

        #self.motionProxy.setStiffnesses("LArm", 1.0)
        time.sleep(4)
        # right = self.recordArmAngles("RArm")
        # print("RArm angles note 1")
        # print(right)

        left = self.recordArmAngles("LArm")
        print("LARm angles note 1")
        print(left)
        self.playSong(self.scale)
        #self.playSong(self.song_1)


    

def main():
    rospy.init_node('notePositions', anonymous=True)
    nao_detect_notes = notePositions()
    rate = rospy.Rate(5)
    # try:
    #     rospy.spin()
    # except KeyboardInterrupt:
    #     print("Shutting down")
    # cv2.destroyAllWindows()
    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_detect_notes.run()
        rate.sleep()


if __name__ == '__main__':
	main()
