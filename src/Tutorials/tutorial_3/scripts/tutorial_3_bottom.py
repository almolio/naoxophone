#!/usr/bin/env python

import rospy
import sys
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 


class tutorial_3_bottom:
    def __init__(self):

        # Subscribe to the bottom camera 
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",Image,self.callback)
        
    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)


        cv2.imshow("Bottom Camera", cv_image)

        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=100)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle outline
                radius = i[2]
                cv2.circle(cv_image, center, radius, (0, 0, 255), 3)

        cv2.imshow("Circular Shapes", cv_image)
        cv2.waitKey(3)

        

def main(args):
    ic = tutorial_3_bottom()
    rospy.init_node('tutorial_3_bottom', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)