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
        self.fractionMaxSpeed = 0.3
        #self.postureProxy.goToPosture("Crouch", 0.5)
        #self.motionProxy.setStiffnesses("LArm",0.0) #Disable stiffness in the arm
        # self.motionProxy.setStiffnesses("LArm", 1.0) #Enable stiffness in the arm
        #self.motionProxy.openHand('LHand')
        #time.sleep(2)
        # self.motionProxy.closeHand("LHand")
        # self.motionProxy.setStiffnesses("LArm", 1.0) #Enable stiffness in the arm
        # time.sleep(2)   
        
        # # Subscribe to the camera 
        # self.bridge = CvBridge()
        # self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback_img)


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
        if chainName == "LArm":
            names = ["LShoulderPitch","LShoulderRoll","LElbowYaw","LElbowRoll","LWristYaw"]
        elif chainName == "RArm":
            names = ["RShoulderPitch","RShoulderRoll","RElbowYaw","RElbowRoll","RWristYaw"]
        useSensorValues = True
        arm_angles = self.motionProxy.getAngles(names,useSensorValues)
        return arm_angles

    def hitNote(self,chainName):
        """
        Position the arm above the note and turn wrist to hit the note
        chainName: LArm or RArm
        """
        frame = motion.FRAME_ROBOT
        useSensorValues = True

        dz = 0.04 # translation axis Z (meters)

        # Motion of Arm with block process
        pathList     = []

        axisMaskList = [motion.AXIS_MASK_VEL]
        timeList     = [[1.0]]         # seconds

        currentPos = self.motionProxy.getPosition("LArm", frame, useSensorValues)
        targetPos = almath.Position6D(currentPos)
        targetPos.z -= dz
        pathList.append(list(targetPos.toVector()))
        print("Move Down")
        self.motionProxy.positionInterpolations([chainName], frame, pathList,
                                    axisMaskList, timeList)
        print("Turn Wrist")
        self.turnWrist(chainName,"Down")
        time.sleep(1)
        self.turnWrist(chainName,"Up")

        currentPos = self.motionProxy.getPosition("LArm", frame, useSensorValues)
        targetPos = almath.Position6D(currentPos)
        targetPos.z += dz
        pathList.append(list(targetPos.toVector()))
        print("Lift arm")
        self.motionProxy.positionInterpolations([chainName], frame, pathList,
                                    axisMaskList, timeList)


    def turnWrist(self,chainName,direction):
        if chainName == "LArm":
            names = ["LWristYaw"]
        elif chainName == "RArm":
            names = ["RWristYaw"]
        if direction == "Down":
            angle=-30
        elif direction == "Up":
            angle==30
        angleLists = [angle*almath.TO_RAD, 0.0]
        timeLists  = [1.0, 2.0]
        isAbsolute = False  #angle relative to current position
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        time.sleep(1.0)

    

        

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


    def playNote2(self,rhythm):
        """
        Plays the second note (D)
        """
        chainName = "LArm"
        frame = motion.FRAME_ROBOT
    
        # tf_note2 = [0.943839, -0.3301, -0.0142126, 0.189212,
        #                 0.319573, 0.922972, -0.214465, 0.191913,
        #                 0.0839126, 0.197878, 0.976628, 0.298834]

        tf_note2 =   [0.976792, -0.148592, -0.154264, 0.189376,
                        0.157645, 0.986321, 0.0481477, 0.196902,
                        0.144999, -0.0713492, 0.986856, 0.308583]

        # tf_hit_note2  = [0.929485, -0.268685, 0.252719, 0.173369,
        #             0.321279, 0.926305, -0.19682, 0.191384,
        #             -0.181213, 0.264135, 0.947309, 0.247428]

        tf_hit_note2 =  [0.949037, -0.219455, 0.226203, 0.172691,
                            0.220388, 0.975177, 0.0214444, 0.19085,
                            -0.225294, 0.0295009, 0.973844, 0.234601]

        fractionMaxSpeed = 0.5
        axisMask         = 63
        self.motionProxy.setTransforms(chainName, frame, tf_note2, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)
        self.motionProxy.setTransforms(chainName, frame, tf_hit_note2, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)
        self.motionProxy.setTransforms(chainName, frame, tf_note2, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)




    def playNote3(self,rhythm):
        """
        Plays the 3rd note (E)
        """
        chainName = "LArm"
        frame = motion.FRAME_ROBOT


        # tf_note3 = [0.943839, -0.3301, -0.0142126, 0.189212,
        #                 0.319573, 0.922972, -0.214465, 0.191913,
        #                 0.0839126, 0.197878, 0.976628, 0.298834]

        tf_note3 =  [0.972296, -0.0507622, -0.228175, 0.212427,
                    0.0643889, 0.996534, 0.0526741, 0.128898,
                    0.22471, -0.0659067, 0.972194, 0.317382]

        # tf_hit_note3  = [0.929485, -0.268685, 0.252719, 0.173369,
        #             0.321279, 0.926305, -0.19682, 0.191384,
        #             -0.181213, 0.264135, 0.947309, 0.247428]


        tf_hit_note3 = [0.973216, -0.143818, 0.179354, 0.186463,
                        0.143313, 0.989551, 0.0158403, 0.146873,
                        -0.179758, 0.0102878, 0.983657, 0.236318]


        fractionMaxSpeed = 0.5
        axisMask         = 63
        self.motionProxy.setTransforms(chainName, frame, tf_note3, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)
        self.motionProxy.setTransforms(chainName, frame, tf_hit_note3, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)
        self.motionProxy.setTransforms(chainName, frame, tf_note3, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)

    def playNote4(self,rhythm):
        """
        Plays the 4th note (F)
        """
        chainName = "LArm"
        frame = motion.FRAME_ROBOT
        # tf_note4 = [0.986033, -0.152749, -0.0663784, 0.204328,
        #             0.143969, 0.982109, -0.12139, 0.153151,
        #             0.0837329, 0.110138, 0.990383, 0.294098]

        tf_note4 = [0.980718, 0.0570774, -0.186906, 0.214758,
                    -0.0425361, 0.995813, 0.0809101, 0.105312,
                    0.190741, -0.0713998, 0.97904, 0.309327]

        # tf_hit_note4 = [0.962463, -0.150178, 0.226077, 0.183066,
        #                 0.201723, 0.953092, -0.225661, 0.166794,
        #                 -0.181583, 0.262795, 0.947611, 0.242724]

        tf_hit_note4 =   [0.983279, -0.0134404, 0.181609, 0.191637,
                        0.00214976, 0.99806, 0.062224, 0.115612,
                        -0.182093, -0.0607932, 0.9814, 0.233236]


        fractionMaxSpeed = 0.5
        axisMask         = 63
        self.motionProxy.setTransforms(chainName, frame, tf_note4, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)
        self.motionProxy.setTransforms(chainName, frame, tf_hit_note4, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)
        self.motionProxy.setTransforms(chainName, frame, tf_note4, fractionMaxSpeed, axisMask)
        time.sleep(rhythm)

    def run(self):
        self.motionProxy.setStiffnesses("LArm", 1.0)
        time.sleep(4)
        current = self.recordTransform("LArm")
        print("Transform")
        print(current)
        self.hitNote("LArm")

        # #self.playInterpolated1
        # self.playNote1(2)
        # self.playNote2(2)
        # self.playNote3(2)
        # self.playNote4(2)


        # # # """ Transform
        # # // R R R x
        # # // R R R y
        # # // R R R z
        # # // 0 0 0 1
        # # """
        chainName = "LArm"
        frame = motion.FRAME_ROBOT
        transform_note_1 = [1, 0, 0, 0,
                            0, 0.866, -0.5, 0,
                            0, 0.5, 0.866, -0.05]

        fractionMaxSpeed = 0.5
        axisMask         = 63
        self.motionProxy.setTransforms(chainName, frame, transform_note_1, fractionMaxSpeed, axisMask)





    def playInterpolated1(self,rythm):
        # Motion of Arms with block process
        frame = motion.FRAME_ROBOT
        effectorList = ["LArm"]
        axisMaskList = [motion.AXIS_MASK_VEL]
        timeList     = [[0.5, 1.0, 1.5, 2.0, 2.5, 3.0]]         # seconds


        transform_note_1 = [0.85052, -0.520852, 0.073002, 0.150683,
                            0.520812, 0.853411, 0.0210918, 0.232483,
                            -0.0732864, 0.0200814, 0.997109, 0.272251]

        dz = 0.05

        pathList = []
        targetLArmTf = almath.Transform(transform_note_1)
        pathList.append(list(targetLArmTf.toVector()))
        #targetLArmTf = almath.Transform(self.motionProxy.getTransform("LArm", frame, useSensorValues))
        #Point 1
        targetLArmTf.r3_c4 -= dz
        pathList.append(list(targetLArmTf.toVector()))
        
        #Point2
        targetLArmTf.r3_c4 -= dz
        pathList.append(list(targetLArmTf.toVector()))

        targetLArmTf.r3_c4 -= dz
        pathList.append(list(targetLArmTf.toVector()))

        targetLArmTf.r3_c4 -= dz
        pathList.append(list(targetLArmTf.toVector()))

        targetLArmTf.r3_c4 -= dz
        pathList.append(list(targetLArmTf.toVector()))
        
        self.motionProxy.transformInterpolations(effectorList, frame, pathList,axisMaskList, timeList)




        # time.sleep(4.0)
        # print("NOTE 0")
        # self.playNote(do_pos,do_tar)
        # time.sleep(1)
        # # print("NOTE 1")
        # self.playNote(re_pos,re_tar)
        # time.sleep(1)
        # print("NOTE 3")
        # self.playNote(mi_pos,mi_tar)
        # time.sleep(1)
        # print("NOTE 4")
        # self.playNote(fa_pos,fa_tar)
        # time.sleep(1)
        # time.sleep(3)
        # self.playNote(position_note_1,hit_note_1)
        #Target positions: Position6D array (x,y,z,wx,wy,wz) in meters and radians
        #  
        #  ShoulderPitch ShoulderRoll ElbowYaw ElbowRoll WrisYaw Hand
        #target = [1.043, 0.264, -2.086, -1.023, 1.39, 0.45]



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
