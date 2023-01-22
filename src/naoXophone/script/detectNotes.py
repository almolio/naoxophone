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
        self.motionProxy.openHand('LHand')
        time.sleep(2)
        self.motionProxy.closeHand('LHand')
        #self.postureProxy.goToPosture("Crouch", 0.5)
        self.motionProxy.setStiffnesses("LHand", 1.0)
        # time.sleep(10)

        # self.motionProxy.setStiffnesses("LShoulder",0.0)

        # # Subscribe to the camera 
        # self.bridge = CvBridge()
        # self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback_img)

        
    def callback_img(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        cv2.imshow("Bottom Camera", cv_image)
        cv2.waitKey(3)
        

    # def joint_state_callback(self):
# 
        # pass

    def recordJointState(self): 

        pass
    def playNote(note,arm,notesTargets,motionProxy):
        target = [1.043, 0.264, -2.086, -1.023, 1.39, 0.45]
        chainName = arm
        frame     = motion.FRAME_TORSO
        target = notesTargets[note,:]
        fractionMaxSpeed = 0.5
        axisMask         = 7 # just control position
        motionProxy.setPositions(chainName, frame, target, fractionMaxSpeed, axisMask)

    def run(self): 
        # self.postureProxy.goToPosture("Stand",1.0)
        # time.sleep(2)
        #self.motionProxy.openHand('RHand')
        #self.motionProxy.closeHand('LHand')
        # time.sleep(2)
        #self.motionProxy.wakeUp()
        #self.motionProxy.rest()
        # self.motionProxy.openHand('LHand')
        # self.motionProxy.closeHand('LHand')
        # self.motionProxy.setStiffnesses('LHand', 1.0)
        chainName = "LArm"
        frame     = motion.FRAME_TORSO
        useSensor = False
        fractionMaxSpeed = 0.5
        axisMask         = 63 # just control position
        print("move arm")
        current = self.motionProxy.getPosition(chainName, frame, useSensor)
        print(current)
        # print("hitnote")
        # time.sleep(7)
        # current = self.motionProxy.getPosition(chainName, frame, useSensor)
        # print(current)
        # self.motionProxy.openHand('LHand')
        # time.sleep(2)
        # self.motionProxy.closeHand('LHand')
        # time.sleep(1.0)

        # self.motionProxy.setStiffnesses("LArm", 0.0)
        # time.sleep(5)
        # self.motionProxy.closeHand('LHand')
        # time.sleep(2)

        # print("moving arm")
        # #target = [0.14297427237033844, 0.1985192894935608, 0.0044593364000320435, -0.5434936285018921, 0.16658470034599304, 0.29215022921562195]
        # target = [0.13655225932598114, 0.1965949833393097, -0.002717709168791771, -0.10835812985897064, 0.015491385012865067, 0.49930909276008606]
        target=[0.1839270293712616, 0.1935415416955948, 0.043190956115722656, -0.05606847256422043, -0.037899136543273926, 0.397024542093277]


        # target_hit= [0.1375078409910202, 0.19652606546878815, -0.0022846711799502373, 0.2099812626838684, 0.011187086813151836, 0.4861317276954651]
        target_hit=[0.17106272280216217, 0.19319814443588257, 0.01128946803510189, 0.30095362663269043, 0.13278625905513763, 0.36690160632133484]
        #Target positions: Position6D array (x,y,z,wx,wy,wz) in meters and radians
        #  
        #  ShoulderPitch ShoulderRoll ElbowYaw ElbowRoll WrisYaw Hand
        #target = [1.043, 0.264, -2.086, -1.023, 1.39, 0.45]
        self.motionProxy.setPositions(chainName, frame, target, fractionMaxSpeed, axisMask)
        #target = [ 0.7761621475219727, 0.6457719802856445, -1.0968518257141113, -0.6120240688323975, 0.817579984664917, 0.6043999791145325]
        time.sleep(3)
        print("Hit note")
        self.motionProxy.setPositions(chainName, frame, target_hit, fractionMaxSpeed, axisMask)
        current = self.motionProxy.getPosition(chainName, frame, useSensor)
        print(current)
        time.sleep(2)




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
