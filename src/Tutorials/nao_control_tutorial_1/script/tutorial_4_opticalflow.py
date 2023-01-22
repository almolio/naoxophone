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


class tutorial_4_opticalflow:

# ADAPTED FROM 
# https://github.com/vanbreugel-lab/optic_flow_example/blob/master/nodes/optic_flow_lucas_kanade.py
# and https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html
################################################################################

    def __init__(self):

        # Subscribe to the top camera 
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/top/camera/image_raw",
                                        Image,self.callback)
        self.prev_image = None
        self.last_time = 0
        
        # Lucas Kanade Optic Flow parameters
        self.lk_params = dict( winSize  = (15,15),
                               maxLevel = 2,
                               criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 
                               10, 0.03))

        # Feature selection parameters 
        self.feature_params = dict( maxCorners = 15,
                       qualityLevel = 0.1,
                       minDistance = 5)
        
        # Flow_mask hold the accumulation of the point track to visualize the flow
        self.flow_mask = None

    def callback(self, image):
        try: # if there is an image
            
            # Acquire the image, and convert to single channel gray image
            raw_img = self.bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")
            curr_image = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('raw image',raw_img)
            
            # If this is the first loop, initialize image matrices
            if self.prev_image is None:
                self.prev_image = curr_image
                # self.points_to_track = define_points_at_which_to_track_optic_flow(curr_image, 50)
                self.points_to_track = cv2.goodFeaturesToTrack(curr_image, 
                                mask = None, 
                                **self.feature_params)
                # NOT SURE IF YOU NEED FLOAT32 HERE

                self.flow_mask = np.zeros_like(raw_img)
                return # skip the rest of this loop
                

            
            # calculate optic flow with lucas kanade
            # see: http://docs.opencv.org/modules/video/doc/motion_analysis_and_object_tracking.html
            new_position_of_tracked_points, status, error = cv2.calcOpticalFlowPyrLK(
                self.prev_image, curr_image, 
                self.points_to_track, None, **self.lk_params)
            
            
            # Select good points 
            if new_position_of_tracked_points is not None:
                good_new_point = new_position_of_tracked_points[status==1]
                good_old_point = self.points_to_track[status==1]

            for i, (new, old) in enumerate(zip(good_new_point, good_old_point)):
                # If you want pretty color 
                # color = np.random.randint(100, 255, (100, 3))
                # draw_color = color[i].tolist()

                draw_color = [0,0,200]
                new_x, new_y = new.ravel()
                old_x, old_y = old.ravel()

                cv2.line(self.flow_mask, 
                    (int(new_x), int(new_y)), 
                    (int(old_x), int(old_y)), 
                   draw_color, 3)

                cv2.circle(raw_img,
                    (int(new_x), int(new_y)), 
                    5, draw_color, -1)                
            
            flow_with_track_point_img = cv2.add(raw_img, self.flow_mask)
            cv2.imshow('Flow with Tracked points', flow_with_track_point_img)

            # Save the image for the next flow itteration
            self.prev_image = curr_image.copy()

            # Some weird operation add a dimension to the middle
            # without this there would be an error
            self.points_to_track = good_new_point.reshape(-1,1,2)
            
        except CvBridgeError as e:
            print (e)

        cv2.waitKey(10) 


class arucodetection:
    # adapted from https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/
    # pose estimation adapted from https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python/blob/main/pose_estimation.py

    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/top/camera/image_raw",
                                        Image,self.callback)
    
        # self.camera_params = []
        self.camera_matrix = np.asarray([[551.543059,0.000000,327.382898], 
                            [0.000000, 553.736023,225.026380 ], 
                            [0.000000,  0.000000, 1.000000]])
        self.distortion_coefficients = np.asarray([-0.066494,0.095481,-0.000279,0.002292,0.000000])

        self.Cx = 0
        self.Cy = 0
        self.raw_img = 0

    def callback (self, image):
        try: # if there is an image
        
        # Acquire the image, and convert to single channel gray image
            
            self.raw_img = self.bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")

        except CvBridgeError as e:
            print (e)

        cv2.waitKey(30)             

    def run(self):
        arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
            # print(arucoDict)

        arucoParams = cv2.aruco.DetectorParameters_create()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(self.raw_img, arucoDict,
            parameters=arucoParams)

        cv2.imshow("Image from NAO", self.raw_img)
        # print('Aruco Corners {},aruco IDS {}'.format(corners,ids))

        image_aruco = self.raw_img.copy()
        if len(corners) > 0:
            # flatten the ArUco IDs list
            ids = ids.flatten()
            # Draw the corners and ids
            image_aruco = self.markerboundary(image_aruco, corners, ids)

            # also draw Detected marker but doesn't give id 
            # cv2.aruco.drawDetectedMarkers(image_aruco, corners) 


            # Call this function to take in the coordinate frame on top of the Aruco
            image_aruco = self.pose_estimation(image_aruco,corners,ids, self.camera_matrix, self.distortion_coefficients)

        cv2.imshow("3D marker position", image_aruco)
        

    def markerboundary(self,image_aruco, corners, ids):
        for (markerCorner, markerID) in zip(corners, ids):
            # extract the marker corners (which are always returned in
            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            cv2.line(image_aruco, topLeft, topRight, (255, 0, 0), 2)
            cv2.line(image_aruco, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(image_aruco, bottomRight, bottomLeft, (0, 0, 255), 2)
            cv2.line(image_aruco, bottomLeft, topLeft, (0, 255, 0), 2)

            # compute and draw the center (x, y)-coordinates of the ArUco
            # marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(image_aruco, (cX, cY), 4, (0, 0, 255), -1)
            # draw the ArUco marker ID on the image
            cv2.putText(image_aruco, 'id = {}'.format(markerID),
                (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
            self.Cx = cX
            self.Cy = cY

        return image_aruco
         

    def pose_estimation(self, frame, corners,ids, camera_matrix, distortion_coefficients):
        # Estimate pose of each marker and return the values rvec and tvec---(different from those of camera coefficients)
        for i in range(len(ids)):
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, camera_matrix,
                                                                        distortion_coefficients)
            # Draw a square around the markers
            # cv2.aruco.drawDetectedMarkers(frame, corners) 
            # print('')
            # Draw Axis
            cv2.aruco.drawAxis(frame, camera_matrix, distortion_coefficients, rvec, tvec, 0.01)  
            # print("Tvec = {}".format(tvec))

        return frame


def main(args):

    # ic = tutorial_4_opticalflow()
    ic = arucodetection()
    rospy.init_node('tutorial_4_opticalflow', anonymous=True)

    try:
        rospy.spin()
    except KeyboardInterrupt: 
        print("Shutting down")
        cv2.destroyAllWindows()



if __name__ == '__main__':
	main(sys.argv)
