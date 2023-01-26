#!/usr/bin/env python2

import rospy
import sys
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 
import imutils

class tutorial_3:
    def __init__(self):

        # Subscribe to the top camera 
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/top/camera/image_raw",Image,self.callback)
        
    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        (rows,cols,channels) = cv_image.shape
        cv2.imshow("Top Camera", cv_image)
        
        cv_image_hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,200,180])
        upper_red = np.array([10,255,255])
        mask = cv2.inRange(cv_image_hsv, lower_red, upper_red)
        cv2.imshow("Color Extraction", mask)	
    
        kernel = np.ones((6, 6), np.uint8)
        kernel[0,0] = kernel[5,0] = kernel[0,5] = kernel[5,5] = 0
        #Erode and dilate 
        
        mask = cv2.erode(mask, None, iterations=2)
        dilated_img = cv2.dilate(mask, kernel, iterations=2)



        cnts = cv2.findContours(dilated_img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        if cnts:
            c = max(cnts, key=cv2.contourArea)
            M = cv2.moments(c)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                temp = np.zeros((cv_image_hsv.shape))
                temp[:,:,0] = dilated_img
                temp[:,:,1] = dilated_img
                temp[:,:,2] = dilated_img
                cv2.circle(temp, (cx, cy), 7, (0, 0, 255), -1)

            cv2.drawContours(temp, [c], -1, (0, 255, 255), 5)
            print("The mass center of the largest blob is: {}, {}".format(cx, cy))
            cv2.imshow("Blob Extraction", temp)  
        
        cv2.waitKey(3)

        

def main(args):
    ic = tutorial_3()
    rospy.init_node('tutorial_3', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)