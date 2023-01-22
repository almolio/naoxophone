#!/usr/bin/env python2
from __future__ import print_function

import roslib
roslib.load_manifest('tutorial_2')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class tutorial_2:
 
	def __init__(self):
	  
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/nao_robot/camera/top/camera/image_raw",Image,self.callback)
	  
	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)
	  
		(rows,cols,channels) = cv_image.shape
		cv2.imshow("Original Image", cv_image)		

 		cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
		cv2.imshow("Greyscale Image", cv_image_grey)	

		cv2.waitKey(3)

		ret,cv_image_binary = cv2.threshold(cv_image_grey,127,255,cv2.THRESH_BINARY)
		cv2.imshow("Binary Image", cv_image_binary)	
	  
	
	  	
def main(args):
	ic = tutorial_2()
	rospy.init_node('tutorial_2', anonymous=True)
	try:
		rospy.spin()
 	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()
	  
if __name__ == '__main__':
	main(sys.argv)

