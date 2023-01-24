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
import cv2


# docs: http://doc.aldebaran.com/2-4/naoqi/motion/control-joint-api.html 
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

class detectNotes:
    def __init__(self):
        self.motionProxy = ALProxy('ALMotion',naoIP, PORT) 
        self.rate = rospy.Rate(1)
        self.postureProxy = ALProxy('ALRobotPosture', naoIP, PORT)
        self.notesTargets=np.zeros((8,6))
        self.notesPositions = np.zeros((8,6))
        self.notesPositions[0,:] = np.array([0.1839270293712616, 0.1935415416955948, 0.043190956115722656, -0.05606847256422043, -0.037899136543273926, 0.397024542093277])
        self.notesTargets[0,:] = np.array([0.17106272280216217, 0.19319814443588257, 0.01128946803510189, 0.30095362663269043, 0.13278625905513763, 0.36690160632133484])
        #self.postureProxy.goToPosture("Crouch", 0.5)
        #self.motionProxy.setStiffnesses(1.0)
        #self.grabStick()
        # self.motionProxy.openHand('LHand')
        # time.sleep(2)
        #self.motionProxy.closeHand("LHand")
        # self.motionProxy.setStiffnesses("LArm", 1.0)
        # time.sleep(10)

        # self.motionProxy.setStiffnesses("LShoulder",0.0)

        # Subscribe to the camera 
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback_img)
    # def grabStick(self):
    #     self.motionProxy.openHand('LHand')
    #     time.sleep(2)
    #     self.motionProxy.closeHand('LHand')


        

        
    def callback_img(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.imshow("Bottom Camera", cv_image)
        cv2.waitKey(3)
        

    def recordJointState(self,chainName): 
        frame= motion.FRAME_ROBOT
        useSensor = False
        current_position = self.motionProxy.getPosition(chainName, frame, useSensor)
        print(type(current_position))
        return current_position

    def playNote(self,notePosition,noteTarget):
        #self.motionProxy.closeHand("LHand")
        chainName = "LArm"
        frame     = motion.FRAME_ROBOT
        useSensor = False
        fractionMaxSpeed = 0.7
        axisMask         = 63 # just control position
        print("move arm")
        current = self.recordJointState("LArm")
        print(current)
        self.motionProxy.setPositions(chainName, frame, notePosition, fractionMaxSpeed, axisMask)
        time.sleep(0.5)
        print("Hit note")
        self.motionProxy.setPositions(chainName, frame, noteTarget, fractionMaxSpeed, axisMask)
        current = self.recordJointState("LArm")
        print(current)
        time.sleep(0.5)
        self.motionProxy.setPositions(chainName, frame, notePosition, fractionMaxSpeed, axisMask)
        time.sleep(2)
    

    def run(self):
        self.motionProxy.setStiffnesses("LArm", 1.0)
        # time.sleep(5)
        # print("note_position")
        # current = self.recordJointState("LArm")
        # print(current)
        # time.sleep(5)
        # print("hitnote")
        # current = self.recordJointState("LArm")
        # print(current)




        note_robot_0=[0.19847379624843597, 0.15, 0.27750444412231445, -0.2221556454896927, 0.06161089241504669, 0.2799208164215088]
        target_robot_0=[0.19636911153793335, 0.15, 0.27133744955062866,  0.3979854881763458, 0.07442747801542282, 0.26681652665138245]



        note_robot_1=[0.19847379624843597, 0.14, 0.27750444412231445, -0.020675629377365112, -0.0529148243367672, 0.2253013551235199]
        target_robot_1=[0.19636911153793335, 0.14, 0.27133744955062866, 0.40429988503456116, -0.005397465545684099, 0.19384582340717316]



        note_robot_2=[0.19847379624843597, 0.13, 0.27750444412231445, -0.020675629377365112, -0.0529148243367672, 0.2253013551235199]
        target_robot_2=[0.19636911153793335, 0.13, 0.27133744955062866, 0.40429988503456116, -0.005397465545684099, 0.19384582340717316]


        position_note_0 = [0.19983044266700745, 0.1661495417356491, 0.313913711309433, -0.10698379576206207, 0.01280924826860428, 0.2896997034549713]

        do_pos=[0.189, 0.19, 0.29, 0.00255, 0.123, 0.539]
        do_tar=[0.210, 0.18, 0.25, 0.5592, 0.1392, 0.22]

        re_pos=[0.225, 0.16, 0.31, 0.00255, 0.233, 0.539]
        re_tar= [0.210, 0.16, 0.24, 0.536399781703949, 0.16790269315242767, 0.2183035597205162]

        mi_pos=[0.208, 0.13, 0.27, 0.00425515517219901085, 0.12331239879131317, 0.23918692767620087]
        mi_tar=[0.204, 0.13, 0.24, 0.5362135787010193, 0.13591791689395905, 0.19782032072544098]

        fa_pos=[0.208, 0.11, 0.27, 0.004095623269677162, 0.12505920231342316, 0.10356026142835617]
        fa_tar= [0.204, 0.11, 0.24, 0.536399781703949, 0.16790269315242767, 0.1183035597205162]


        hit_note_0 = [0.19492362439632416, 0.1593276858329773, 0.25232091546058655, 0.4199238717556, 0.22625409066677094, 0.22365818917751312]

        position_note_1 = [0.19983044266700745, 0.1461495417356491, 0.313913711309433, -0.10698379576206207, 0.01280924826860428, 0.2896997034549713]

        hit_note_1 = [0.19492362439632416, 0.1393276858329773, 0.25232091546058655, 0.4199238717556, 0.22625409066677094, 0.22365818917751312]

        position_note_2 = [0.181898798942566, 0.185, 0.07, -0.06518647819757462, 0.0058492752723395824, 0.44996950030326843]

        hit_note_2 = [0.18825254678726196, 0.185, 0.07, 0.302416871190071106, 0.00849573157727718, 0.3333791434764862]

        # position_note_2 = [0.161898798942566, 0.15266318202018738, 0.105748122707009315, 0.1199328824877739, -0.05328581511974335, 0.37284886837005615]

        # hit_note_2 = [0.16825254678726196, 0.15280106246471405, -0.011986449137330055, 0.16163532435894012, -0.014630560763180256, 0.37130504846572876]

        print("NOTE 0")
        self.playNote(do_pos,do_tar)
        time.sleep(1)
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
     




##############
# SEND MOVEMENT TO NAO 
##############

    # def send_movement(req):
    #     print(req, type(req.joint_name), type(req.angle), type(req.speed))

    #     if(req.relative):
    #         print("Setting relative position to follow marker")
    #         cur_angle = motionProxy.getAngles(req.joint_name, False)
    #         req.angle = cur_angle[0]*almath.TO_DEG + req.angle
        
    #     req = check_limits(req)
    #     motionProxy.setAngles(req.joint_name, req.angle*almath.TO_RAD, req.speed)
    #     print(motionProxy.getTaskList())
    # #    time.sleep(3.0)

        #disable = rospy.ServiceProxy('body_stiffness/disable', Empty)
        #disable()
        # return True



def main():
    rospy.init_node('detectNotes', anonymous=True)
    nao_detect_notes = detectNotes()
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
