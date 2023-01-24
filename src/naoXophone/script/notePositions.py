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
        self.rate = rospy.Rate(1)
        self.postureProxy = ALProxy('ALRobotPosture', naoIP, PORT)
        self.notesTargets=np.zeros((8,6))
        self.notesPositions = np.zeros((8,6))
        self.notesPositions[0,:] = np.array([0.1839270293712616, 0.1935415416955948, 0.043190956115722656, -0.05606847256422043, -0.037899136543273926, 0.397024542093277])
        self.notesTargets[0,:] = np.array([0.17106272280216217, 0.19319814443588257, 0.01128946803510189, 0.30095362663269043, 0.13278625905513763, 0.36690160632133484])
        #self.postureProxy.goToPosture("Crouch", 0.5)
        #self.motionProxy.setStiffnesses(1.0)
        # #self.grabStick()
        # self.motionProxy.openHand('LHand')
        # time.sleep(2)
        self.motionProxy.closeHand("LHand")
        self.motionProxy.setStiffnesses("LArm", 1.0)
        # time.sleep(10)

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
        # self.motionProxy.setStiffnesses("LArm", 1.0)
        time.sleep(4)
        # time.sleep(5)
        # print("note_position")
        # current = self.recordJointState("LArm")
        # print(current)
        # time.sleep(5)
        # print("hitnote")
        # current = self.recordJointState("LArm")
        # print(current)

        # # # Example showing how to set Torso Transform, using a fraction of max speed
        chainName        = "LArm"
        frame            = motion.FRAME_ROBOT

        # # """ Transform
        # # // R R R x
        # # // R R R y
        # # // R R R z
        # # // 0 0 0 1
        # # """
        transform        = [1.0, 0.0, 0.0, 0.40,    
                            0.0, 1.0, 0.0, 0.35,
                            0.0, 0.0, 1.0, 0.35]

        transform_hit   = [1.0, 0.0, 0.0, 0.40,    
                            0.0, 1.0, 0.0, 0.35,
                            0.0, 0.0, 1.0, 0.25]

        transfor_2        = [1.0, 0.3, 0.0, 0.40,    
                            0.3, 1.0, 0.0, 0.25,
                            0.0, 0.0, 1.0, 0.35]

        transform_hit_2   = [1.0, 0.0, 0.0, 0.45,    
                            0.0, 1.0, 0.0, 0.25,
                            0.0, 0.0, 1.0, 0.25]

        transform_note1   =  [0.842626, -0.412946, 0.345625, 0.149998,
                            0.357341, 0.908939, 0.214793, 0.210217,
                            -0.40285, -0.0574843, 0.913459, 0.278304]

        transform_hit_note1   =  [0.842626, -0.412946, 0.345625, 0.149998,
                            0.357341, 0.908939, 0.214793, 0.200217,
                            -0.40285, -0.0574843, 0.913459, 0.218304]

        transform_hit_note1   =[0.896099, -0.226726, 0.381578, 0.163841,
                            0.315852, 0.929728, -0.189322, 0.221143,
                            -0.31184, 0.290173, 0.904741, 0.242694]


        tf_note2   =  [0.842626, -0.412946, 0.345625, 0.149998,
                            0.357341, 0.908939, 0.214793, 0.220217,
                            -0.40285, -0.0574843, 0.913459, 0.218304]

        tf_hit2   =[0.896099, -0.226726, 0.381578, 0.163841,
                            0.315852, 0.929728, -0.189322, 0.221143,
                            -0.31184, 0.290173, 0.904741, 0.182694]



        fractionMaxSpeed = 0.5
        axisMask         = 63
        useSensorValues = False

        # print("Init")
        self.motionProxy.setTransforms(chainName, frame, transform_note1, fractionMaxSpeed, axisMask)
        time.sleep(4)
        self.motionProxy.setTransforms(chainName, frame, transform_hit_note1, fractionMaxSpeed, axisMask)
        print("Hit note")
        # self.motionProxy.setTransforms(chainName, frame, transform_hit, fractionMaxSpeed, axisMask)
        # # self.motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        # # time.sleep(4)
        # # self.motionProxy.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
        # print("Move Finished")
        # time.sleep(4)


        # print("Init 2")
        # self.motionProxy.setTransforms(chainName, frame, transfor_2, fractionMaxSpeed, axisMask)
        # time.sleep(4)
        # print("Hit 2")
        # self.motionProxy.setTransforms(chainName, frame, transform_hit_2, fractionMaxSpeed, axisMask)
        # # time.sleep(4)
        # # self.motionProxy.setTransforms(chainName, frame, transfor_2, fractionMaxSpeed, axisMask)
        # print("Move 2 Finished")
        # time.sleep(4)



        # # Motion of Arms with block process
        # effectorList = ["LArm"]
        # axisMaskList = [motion.AXIS_MASK_VEL]
        # timeList     = [[1.0, 2.0, 3.0]]         # seconds

        # # targetLArmTf = [1.0, 0.0, 0.0, 0.40,    
        # #                 0.0, 1.0, 0.0, 0.35,
        # #                 0.0, 0.0, 1.0, 0.35]
        # dz = 0.05

        # pathList = []
        # targetLArmTf = almath.Transform(transform)
        # pathList.append(list(targetLArmTf.toVector()))
        # #targetLArmTf = almath.Transform(self.motionProxy.getTransform("LArm", frame, useSensorValues))
        # #Point 1
        # targetLArmTf = almath.Transform(transform_hit)
        # targetLArmTf.r3_c4 -= dz
        # pathList.append(list(targetLArmTf.toVector()))
        
        # #Point 2
        # targetLArmTf = almath.Transform(transform)
        # targetLArmTf.r3_c4 -= dz
        # pathList.append(list(targetLArmTf.toVector()))


        # self.motionProxy.transformInterpolations(effectorList, frame, pathList,
        #                                 axisMaskList, timeList)

        # pathList = []
        # targetLArmTf = almath.Transform(transfor_2)
        # pathList.append(list(targetLArmTf.toVector()))
        # #targetLArmTf = almath.Transform(self.motionProxy.getTransform("LArm", frame, useSensorValues))
        # #Point 1
        # targetLArmTf = almath.Transform(transform_hit_2)
        # targetLArmTf.r3_c4 -= dz
        # pathList.append(list(targetLArmTf.toVector()))
        
        # #Point 2
        # targetLArmTf = almath.Transform(transfor_2)
        # targetLArmTf.r3_c4 -= dz
        # pathList.append(list(targetLArmTf.toVector()))


        # self.motionProxy.transformInterpolations(effectorList, frame, pathList,
        #                                 axisMaskList, timeList)

                            

        # transform_note = almath.Transform([0.894376277923584, -0.4424368739128113, -0.06588573008775711, 0.1553073525428772, 
        #                     0.4450879693031311, 0.8948973417282104, 0.032487720251083374, 0.20851591229438782,
        #                     0.04458719491958618, -0.05838119238615036, 0.9972982406616211, 0.26008081436157227,
        #                       0.00, 0.00, 0.00, 1.00]) 
        
        
        # current_transform = almath.Transform(self.motionProxy.getTransform(chainName,frame,useSensorValues)).reshape([4,4])
        print(almath.Transform(self.motionProxy.getTransform(chainName,frame,useSensorValues)))   








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
