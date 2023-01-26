#!/usr/bin/env python

import rospy
import sys
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 
from pathlib import Path
import matplotlib.pyplot as plt
import argparse

class tutorial_4:
    def __init__(self):

        # Subscribe to the top camera 
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/top/camera/image_raw",Image,self.callback)
        
    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)


        ### 1-4 Image processing with still image
        cwd = Path.cwd()
        imgpath = Path.joinpath(cwd,'src/tutorial_3/scripts/templateImg.jpg')
        imgraw = cv2.imread(str(imgpath), cv2.IMREAD_COLOR)
        x_1,y_1=105,65
        x_2,y_2 = 215,210
        cv2.rectangle(imgraw, (x_1,y_1), (x_2,y_2), (255,0,0), 2)
        cv2.imshow("Image with ROI", imgraw)
        image_hsv = cv2.cvtColor(imgraw, cv2.COLOR_BGR2HSV)
        hsv_planes = cv2.split(image_hsv)
        cv2.imshow("Saturation",hsv_planes[1])
        lower_s = 175
        upper_s = 255
        ret,img_th1 = cv2.threshold(hsv_planes[1],lower_s,upper_s,cv2.THRESH_BINARY) # img_th1 is a saturation mask
        
        #Calculate and normalize histogram
        hist_size = 64
        s_hist = cv2.calcHist(hsv_planes, [1], img_th1, [hist_size],[0,256], accumulate = True)
        hist_w = 256
        hist_h = 256
        bin_w = int(round( hist_w/hist_size))
        histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
        
        cv2.normalize(s_hist, s_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
        #cv2.normalize(s_hist, s_hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        #print("Normalize hist {}".format(s_hist))

        #Draw histogram
        for i in range(1, hist_size):
            cv2.line(histImage, (bin_w*(i-1), hist_h - int(s_hist[i-1]) ),
                ( bin_w*(i), hist_h - int(s_hist[i]) ),
                ( 255, 0, 0), thickness=2)
        cv2.imshow('Normalized histogram', histImage)


        ## 5. Process with new image 
        cv2.imshow('Original Image', cv_image)
        cv_image_hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
         
        cv2.imshow('HSV Image', cv_image_hsv)
        img_hsv_split= cv2.split(cv_image_hsv) 
        # sat_upperbound = 215
        # sat_lowerbound = 150


        ## 6. apply meanshift to get the new location
        x,y=105,65
        w,h = 215-x,210-y
        track_window = (x, y, w, h)
        track_window_cs = (x,y,w,h)
        roi = image_hsv[y:y+h, x:x+w] #Take ROI from the template image
        roi_hsv_split= cv2.split(roi) 
        hue_range = [90,110]
        
        _, sat_mask_obj = cv2.threshold(roi_hsv_split[1],lower_s,upper_s,cv2.THRESH_BINARY)
        _, hue_mask_obj = cv2.threshold(roi_hsv_split[0],hue_range[0],hue_range[1],cv2.THRESH_BINARY)
        #sat_mask_obj = cv2.inRange(roi_hsv_split[1], lower_s, upper_s)
        _, sat_mask = cv2.threshold(cv_image_hsv[:,:,1],lower_s,upper_s,cv2.THRESH_BINARY)
        _, hue_mask = cv2.threshold(cv_image_hsv[:,:,0],hue_range[0],hue_range[1],cv2.THRESH_BINARY)
        
        #Use ROI from template to calculate histogram
        cv2.imshow('Mask sat', sat_mask_obj)
        roi_hist = cv2.calcHist(roi_hsv_split, [1], sat_mask_obj & hue_mask_obj, [hist_size],[lower_s,upper_s], accumulate = True)
        cv2.normalize(roi_hist,roi_hist,alpha=0,beta=hist_h,norm_type=cv2.NORM_MINMAX)


        #Use ROI histogram to calculat backprojection on the whole image
        backproj = cv2.calcBackProject(img_hsv_split,[1],roi_hist,[lower_s, upper_s],scale=1)
        bitwise_ = cv2.bitwise_and(backproj, sat_mask&hue_mask)
        cv2.imshow('backproj', backproj)
        cv2.imshow('Bitwise', bitwise_)

        
        # Setup the termination criteria, either 10 iteration or move by at least 1 pt
        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
        # apply meanshift to get the new location
        ret_ms, track_window = cv2.meanShift(bitwise_, track_window, term_crit)
        x,y,w,h = track_window
        img_ms = cv2.rectangle(cv_image.copy(), (x,y), (x+w,y+h), 255,2)
        cv2.imshow('meanshift', img_ms)



        #7. CAM-SHIFT ALGORITHM
        ret_cs, track_window_cs = cv2.CamShift(bitwise_, track_window_cs, term_crit)
        pts = cv2.boxPoints(ret_cs)
        pts = np.int0(pts)
        img_cs = cv2.polylines(cv_image.copy(),[pts],True, 255,2)
        cv2.imshow('camshift',img_cs)
    
        cv2.waitKey(3)
        
def main(args):
    ic = tutorial_4()
    rospy.init_node('tutorial_4', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
