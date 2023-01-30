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
        self.fractionMaxSpeed = 0.2
        self.notePosition1 = [0.3589141368865967, 0.5302840347290039, -1.0078802108764648, -0.4662940502166748, 0.7853660583496094]
        self.notePosition2 = [0.3589141368865967, 0.4432840347290039, -1.0078802108764648, -0.4662940502166748, 0.7853660583496094]
        self.notePosition3 = [0.2709141368865967, 0.2682840347290039, -1.0078802108764648, -0.4662940502166748, 0.7853660583496094]
        self.notePosition4 = [0.2709141368865967, 0.1832840347290039, -1.0078802108764648, -0.4662940502166748, 0.7853660583496094]
        self.notePosition5 = [0.28690004348754883, 0.05058002471923828, 1.483336091041565, 0.357464075088501, -1.3683700561523438]
        self.notePosition6 = [0.28690004348754883, -0.05058002471923828, 1.483336091041565, 0.357464075088501, -1.3683700561523438]
        self.notePosition7 = [0.35690004348754883, -0.12458002471923828, 1.483336091041565, 0.357464075088501, -1.3683700561523438]
        self.notePosition8 = [0.35690004348754883, -0.20958002471923828, 1.483336091041565, 0.357464075088501, -1.3683700561523438]
        #self.motionProxy.rest()
        self.motionProxy.setStiffnesses("Body",1.0)
        # time.sleep(2)
        #self.postureProxy.goToPosture("Crouch", 0.5)
        self.motionProxy.setAngles("LHipYawPitch", -0.190174, self.fractionMaxSpeed)
        # self.motionProxy.setStiffnesses("LArm",0.0) #Disable stiffness in the arm
        # self.motionProxy.setStiffnesses("RArm",0.0) #Disable stiffness in the arm

        # # self.motionProxy.setStiffnesses("LArm", 1.0) #Enable stiffness in the arm
        # self.motionProxy.openHand('LHand')
        # time.sleep(2)
        # self.motionProxy.closeHand("LHand")
        # self.motionProxy.setStiffnesses("LArm", 1.0) #Enable stiffness in the arm
        # time.sleep(2)   
        
        # Subscribe to the camera 
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback_img)


    def grabStick(self):
        self.motionProxy.openHand('LHand')
        time.sleep(2)
        self.motionProxy.closeHand('LHand')

        
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

    def hitNote(self,chainName,notePosition):
        """
        Position the arm above the note and turn wrist and shoulder to hit the note
        chainName: LArm or RArm
        notePosition: init position for the note
        """
        if chainName == "LArm":
            names = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
        elif chainName == "RArm":
            names = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
        self.motionProxy.angleInterpolationWithSpeed(names, notePosition, self.fractionMaxSpeed)

        axisMaskList = [motion.AXIS_MASK_VEL]
        timeList     = [[1.0]]         # seconds

        ## Move arm to position above note
        # self.motionProxy.angleInterpolation([chainName], frame, notePosition,
        #                             axisMaskList, timeList)
        self.turnDown(chainName)
        #self.motionProxy.angleInterpolationWithSpeed(names, notePosition, self.fractionMaxSpeed)
        time.sleep(1.0)


    def turnDown(self,chainName):
        wrist_angle=0.0
        names=[]
        if chainName == "LArm":
            names = ["LWristYaw", "LShoulderPitch"]
            wrist_angle=20.0
            shoulder_angle = 20
        elif chainName == "RArm":
            names = ["RWristYaw", "RShoulderPitch"]
            wrist_angle=-20.0
            shoulder_angle = 20

        angleLists  = [[wrist_angle*almath.TO_RAD, 0.0], [shoulder_angle*almath.TO_RAD, 0.0]]
        timeLists   = [[1.0, 2.0], [ 1.0, 2.0]]
        isAbsolute = False  #angle relative to current position
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    

    def recordTransform(self,chainName): 
        chainName = "LArm"
        frame = motion.FRAME_ROBOT
        useSensorValues = False
        tf = almath.Transform(self.motionProxy.getTransform(chainName,frame,useSensorValues))
        return tf

    # def playNote(self,notePosition,noteTarget):
    #     #self.motionProxy.closeHand("LHand")State("LArm")
    #     useSensor = False
    #     fractionMaxSpeed = 0.7
    #     axisMask         = 63 # just control position
    #     print("move arm")
    #     current = self.recordJointState("LArm")
    #     print(current)
    #     self.motionProxy.setPositions(chainName, frame, notePosition, fractionMaxSpeed, axisMask)
    #     time.sleep(0.5)
    #     print("Hit note")
    #     self.motionProxy.setPositions(chainName, frame, noteTarget, fractionMaxSpeed, axisMask)
    #     current = self.recordJointState("LArm")
    #     print(current)
    #     time.sleep(0.5)
    #     self.motionProxy.setPositions(chainName, frame, notePosition, fractionMaxSpeed, axisMask)
    #     time.sleep(2)


    def playNote1(self,rhythm):
        """
        Plays the first note (C)
        """
        chainName = "LArm"
        frame = motion.FRAME_ROBOT
        # transform_note_1 = [0.85052, -0.520852, 0.073002, 0.150683,
        #                     0.520812, 0.853411, 0.0210918, 0.232483,
        #                     -0.0732864, 0.0200814, 0.997109, 0.272251]

        transform_note_1  = [0.949419, -0.313825, -0.010873, 0.165477,
                            0.314006, 0.949064, 0.0260411, 0.178851,
                            0.00214686, -0.0281381, 0.999602, 0.286437]


        # transform_hit_note1 = [0.807697, -0.513714, 0.289352, 0.135345,
        #                     0.546821, 0.836205, -0.0418006, 0.234763,
        #                     -0.220484, 0.191986, 0.95631, 0.244178]

        transform_hit_note1 = [0.900836, -0.32807, 0.284367, 0.162335,
                                0.335875, 0.941641, 0.0223509, 0.183376,
                                -0.275105, 0.0753773, 0.958455, 0.232225]


        # transform_hit_note1   =[0.896099, -0.226726, 0.381578, 0.163841,
        #                         0.315852, 0.929728, -0.189322, 0.221143,
        #                         -0.31184, 0.290173, 0.904741, 0.242694]
        fractionMaxSpeed = 0.3
        axisMask         = 63

        self.motionProxy.setTransforms(chainName, frame, transform_note_1, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)
        self.motionProxy.setTransforms(chainName, frame, transform_hit_note1, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)
        self.motionProxy.setTransforms(chainName, frame, transform_note_1, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)

    def run(self):
        # self.motionProxy.setStiffnesses("LArm",1.0) #Disable stiffness in the arm
        # self.motionProxy.setStiffnesses("RArm",1.0) #Disable stiffness in the arm

        #self.motionProxy.setStiffnesses("LArm", 1.0)
        time.sleep(4)
        # current = self.recordTransform("LArm")
        current = self.recordArmAngles("RArm")
        print("RArm angles note 1")
        print(current)

        self.hitNote("LArm",self.notePosition1)
        time.sleep(2)
        self.hitNote("LArm",self.notePosition3)
        time.sleep(2)
        self.hitNote("LArm",self.notePosition2)
        time.sleep(2)
        self.hitNote("LArm",self.notePosition4)

        self.hitNote("RArm",self.notePosition5)
        time.sleep(2)
        self.hitNote("RArm",self.notePosition6)
        time.sleep(2)
        self.hitNote("RArm",self.notePosition7)
        time.sleep(2)
        self.hitNote("RArm",self.notePosition8)


    

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
