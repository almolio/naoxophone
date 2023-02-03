#!/usr/bin/env python

import rospy
import qi
from naoqi import ALProxy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from naoXophone.srv import stickCheck
from std_srvs.srv import *
import numpy as np
import cv2
import os
from naoqi_bridge_msgs.msg import HeadTouch, SetSpeechVocabularyActionGoal,SpeechWithFeedbackActionGoal,WordRecognized

naoIP = str(os.getenv("NAO_IP"))
PORT = 9559

class checkSticks:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback_img)
        self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.postureProxy = ALProxy('ALRobotPosture', naoIP, PORT)
        #Text to be said by NAO
        self.speech_pub = rospy.Publisher("/speech_action/goal", SpeechWithFeedbackActionGoal, queue_size=50)
        #Words recognized by NAO
        self.vocab_pub = rospy.Publisher('/speech_vocabulary_action/goal',SetSpeechVocabularyActionGoal, queue_size=50)

    def talk(self,message, goal_id):
        sentence = SpeechWithFeedbackActionGoal()
        sentence.goal_id.id = goal_id
        sentence.goal.say = message
        print(sentence)    
        self.speech_pub.publish(sentence)

    def extract_shapes(self, mask, er, dil, kernel):
        erosion = cv2.erode(mask,kernel,iterations = er)
        dilation = cv2.dilate(erosion,kernel,iterations = dil)
        return dilation

    def callback_img(self, data):
        try:
            self.base_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            base_image = self.base_image
            image_rgb = cv2.cvtColor(base_image, cv2.COLOR_BGR2RGB)
            image_hsv   = cv2.cvtColor(base_image, cv2.COLOR_BGR2HSV)
            lower_black = np.array([50,0,0])
            upper_black = np.array([200,80,80])
            mask_black  = cv2.inRange(image_hsv, lower_black, upper_black)
            # kernel_cir  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
            # dil_black   = self.extract_shapes(mask_black, 1, 1, mask_black)

            #Draw 2 circle on the extracted shape. This circle is fixed. 
            # stickRcenter = (202,100)
            # stickLcenter = (90,92)
            # radiusR = 10
            # radiusL = 10
            # color = (255,255,255)
            # print(dil_black.shape)
            # Set everythign outside the box equal 0 
            # cv2.circle(mask_black, stickRcenter, radiusR, color, -1)
            # cv2.circle(mask_black, stickLcenter, radiusL, color, -1)
        
            # Draw Rectangular for recognition 
            lt = [62, 55] 
            br = [243,150]
            mask_black[:lt[1],:] = 0  
            mask_black[br[1]:,:] = 0 
            mask_black[:,:lt[0]] = 0 
            mask_black[:,br[0]:] = 0

            # TODO: ADJUST THIS FOR LIGHTING
            circle_threshold = 100000 # Total pixel that's white
            # print(np.sum(mask_black))

            # If the stickhead is outside of the predefined spot, the total will increase
            if (np.sum(mask_black) > circle_threshold) :
                self.is_grab = True

            else: self.is_grab = False

            # cv2.imshow("RawImage", image_hsv)
            cv2.imshow("Dilblack", mask_black)
            print(self.is_grab)

        except CvBridgeError as e:
            print(e)
        cv2.waitKey(1)

    

    def service_handle(self,req):
        if self.is_grab:
            message = "Alright, sticks in hand. Ready to play."
            self.talk(message, "stickinhand")

        else: 
            message = "I'm clumsy, and drop the stick! Can you help me? "
            self.talk(message, "restick")
        return []


def main():

    rospy.init_node('checkStick_server', anonymous=True)
    nao_check_stick = checkSticks()
    rate = rospy.Rate(5)

    # if nao_grab_stick.TROUBLESHOOT:
    s = rospy.Service('checkSticks', Empty, nao_check_stick.service_handle)

    while not rospy.is_shutdown(): 
        # nao_grab_stick.runloop()
        rate.sleep()



if __name__ == '__main__':
	main()