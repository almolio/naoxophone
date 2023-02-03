#!/usr/bin/env python

import rospy
import qi
from naoqi import ALProxy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from naoXophone.srv import stickCheck
import numpy as np
import cv2

naoIP = str(os.getenv("NAO_IP"))

class checkSticks:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback_img)
        self.stickcoor = np.zeros([2,2]) # stick x coordinate 


    def callback_img(self, data):
        try:
            self.base_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            image_rgb = cv2.cvtColor(base_image, cv2.COLOR_BGR2RGB)
            image_hsv   = cv2.cvtColor(base_image, cv2.COLOR_BGR2HSV)
            lower_black = np.array([0,0,0])
            upper_black = np.array([150,100,100])
            mask_black  = cv2.inRange(image_hsv, lower_black, upper_black)
            kernel_cir  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
            dil_black   = extract_shapes(mask_black, 1, 3, kernel_cir)

            #Draw 2 circle on the extracted shape. This circle is fixed. 
            stick1center = (50,52)
            stick2center = (100,100)
            radius = 10
            color = (0,0,0)
            cv.circle(dil_black, stick1center, radius, color, -1)
            cv.circle(dil_black, stick2center, radius, color, -1)

            circle_threshold = 100

            if (np.sum(dil_black) < circle_threshold) :
                self.is_grab = True

                else: self.is_grab = False

        except CvBridgeError as e:
            print(e)
           cv2.waitKey(1)

    

    def service_handle(self,req):

        return self.is_grab


def main():

    rospy.init_node('checkStick_server', anonymous=True)
    nao_check_stick = checkSticks()
    rate = rospy.Rate(5)

    # if nao_grab_stick.TROUBLESHOOT:
    s = rospy.Service('checkStick', stickCheck, nao_check_stick.service_handle)

    while not rospy.is_shutdown(): 
        # nao_grab_stick.runloop()
        rate.sleep()



if __name__ == '__main__':
	main()