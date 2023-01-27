#!/usr/bin/env python

import rospy
import sys
import cv2
from std_msgs.msg import String
import motion
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 
from pathlib import Path
import matplotlib.pyplot as plt
import tf

# TNOTES: 
# this is the frame of which this code establish. 
# rosrun tf tf_echo /TOPCAMERAFRAME /ARUCOFRAME
# rosrun tf tf_echo /CameraBottom_frame /ARUCOFRAME
# CameraBottom_frame

# Set the map frame, ie, world frame to a reference frame of robot 
# static_transform_publisher x y z yaw pitch roll frame_id child_frame_id period_in_ms
# run like this: 
# rosrun tf static_transform_publisher 0.0 0 0.0 0.0 0.0 0.0 map CameraTop_frame 180

# run rviz GUI
# rosrun rviz rviz

class arucodetection:
    # adapted from https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/
    # pose estimation adapted from https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python/blob/main/pose_estimation.py

    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/nao_robot/camera/bottom/camera/image_raw",
                                        Image,self.callback)
        self.pub = rospy.Publisher('aruco_coordinate', String, queue_size=10)
        self.tfbroadcaster = tf.TransformBroadcaster()
        # self.camera_params = []
        # self.camera_matrix = np.asarray([[551.543059,0.000000,327.382898], 
        #                                 [0.000000, 553.736023,225.026380 ], 
        #                                  [0.000000,  0.000000, 1.000000]])
        # self.distortion_coefficients = np.asarray([-0.066494,0.095481,-0.000279,0.002292,0.000000])
        self.camera_matrix  = np.asarray([[278.236008818534, 0,    156.194471689706],
                                            [0, 279.380102992049, 126.007123836447],
                                            [0,                0,                1]])
        self.distortion_coefficients   = np.asarray([ -0.0481869853715082,  0.0201858398559121, 
                                                        0.0030362056699177, -0.00172241952442813, 0 ])

        self.cx = 0
        self.cy = 0
        self.tvec = 0
        self.rvec = 0
        self.arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)


    def callback (self, image):
        try: # if there is an image
        
        # Acquire the image, and convert to single channel gray image
            raw_img = self.bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")

            arucoParams = cv2.aruco.DetectorParameters_create()
            (corners, ids, rejected) = cv2.aruco.detectMarkers(raw_img, self.arucoDict,
                parameters=arucoParams)

            cv2.imshow("Image from NAO", raw_img)
            # print('Aruco Corners {},aruco IDS {}'.format(corners,ids))

            image_aruco = raw_img.copy()
            
            if len(corners) > 0:
                # flatten the ArUco IDs list
                ids = ids.flatten()
                # Draw the corners and ids
                image_aruco = self.markerboundary(image_aruco, corners, ids)

                # also draw Detected marker but doesn't give id 
                # cv2.aruco.drawDetectedMarkers(image_aruco, corners) 

                # Call this function to take in the coordinate frame on top of the Aruco
                image_aruco = self.pose_estimation(image_aruco,corners,ids, self.camera_matrix, self.distortion_coefficients)
                # print(type(self.tvec))
                # print((self.tvec.shape))
                roll, pitch, yaw = self.rvec.squeeze()
                self.tfbroadcaster.sendTransform(
                    translation=self.tvec.squeeze(), 
                    rotation= tf.transformations.quaternion_from_euler(roll, pitch, yaw), 
                    time = rospy.get_rostime(),
                    child = 'ARUCOFRAME',
                    # parent = 'TOPCAMERAFRAME')
                    parent= 'CameraBottom_optical_frame')
                    #parent= 'CameraTop_frame')
                

            cv2.imshow("3D marker position", image_aruco)
            string_to_publish = '{} {}'.format(self.cx, self.cy)
            self.pub.publish(string_to_publish)
            # self rvec is the rotation angle, and tvec is the translation 

        except CvBridgeError as e:
            print (e)

        cv2.waitKey(5)             

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
            # cv2.putText(image_aruco, 'id = {}'.format(markerID),
            #     (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
            #     1, (0, 255, 0), 2)
            self.cx = cX
            self.cy = cY
        return image_aruco
         

    def pose_estimation(self, frame, corners,ids, camera_matrix, distortion_coefficients):
        # Estimate pose of each marker and return the values rvec and tvec---(different from those of camera coefficients)
        for i in range(len(ids)):
            self.rvec, self.tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, camera_matrix,
                                                                        distortion_coefficients)


            # Draw Axis
            cv2.aruco.drawAxis(frame, camera_matrix, distortion_coefficients, self.rvec, self.tvec, 0.01)  

        return frame


def main(args):

    ic = arucodetection()
    rospy.init_node('ArucoBroadcast', anonymous=True)

    try:
        rospy.spin()
    except KeyboardInterrupt: 
        print("Shutting down")
        cv2.destroyAllWindows()



if __name__ == '__main__':
	main(sys.argv)