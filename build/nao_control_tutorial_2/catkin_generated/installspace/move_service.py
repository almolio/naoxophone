#!/usr/bin/env python2
import rospy
import time
import motion
import numpy as np
import almath
from std_msgs.msg import String
import sys
from naoqi import ALProxy
from nao_control_tutorial_2.srv import MoveJoints, MoveJointsResponse
import tf
# motionProxy =0
naoIP = '10.152.246.59' #81

class pose_service():
    def __init__(self):

        self.motionProxy = ALProxy('ALMotion',naoIP, 9559)

        self.rate = rospy.Rate(200)

        
        #Start Services
        self.PoseService = rospy.Service("Pose6D", MoveJoints, self.handle_pose)
        # self.matrix = self.get_transform()
        self.pose = None

        
    def handle_pose(self, req):
        print(req)
        joint_requested = req.joint_name 
        postureProxy = ALProxy("ALRobotPosture", naoIP, 9559)

        ##################### make robot stand up #####################
        # self.motionProxy.wakeUp()
        # time.sleep(2.0)
        # postureProxy.goToPosture("StandInit", 0.5)
        ###############################################################
        frame = motion.FRAME_TORSO
        useSensorValues = True
        
        # time.sleep(2.0)
        x_pos = float(req.x_pos)
        y_pos = float(req.y_pos)
        z_pos = float(req.z_pos)
        x_rot = float(req.x_rot)
        y_rot = float(req.y_rot)
        z_rot = float(req.z_rot)
        max_vel = float(req.max_vel)
        exe_time = float(req.exe_time)

        target = [x_pos, y_pos, z_pos, x_rot, y_rot, z_rot]
        


        current_pose = self.motionProxy.getPosition(joint_requested, frame, useSensorValues) 

        if exe_time == 0.0:
            for i in range(6):
                current_pose[i] = current_pose[i]-target[i]
            self.motionProxy.setPositions(joint_requested, frame, current_pose, max_vel, 7)

        else:
            effectorList = []
            pathList     = []

            axisMaskList = [motion.AXIS_MASK_VEL]
            timeList     = [[exe_time]]

            effectorList.append(joint_requested)
            currentPos = self.motionProxy.getPosition(joint_requested, frame, useSensorValues)
            targetPos = almath.Position6D(currentPos)
            targetPos.x -= x_pos
            targetPos.y -= y_pos
            targetPos.z -= z_pos
            pathList.append(list(targetPos.toVector()))

            self.motionProxy.positionInterpolations(effectorList, frame, pathList,
                                        axisMaskList, timeList)


        time.sleep(0.01)

        current_pose = self.motionProxy.getPosition(joint_requested, frame, useSensorValues)

        ##################### make robot sit down #####################
        # self.motionProxy.rest()
        # postureProxy.goToPosture("StandInit", 0.5)
        ###############################################################
        return MoveJointsResponse(current_pose[0],current_pose[1],current_pose[2], \
        current_pose[3],current_pose[4],current_pose[5])


    # def get_transform(self):

    #     tflistener = tf.TransformListener()

    #     (trans,rot) = tflistener.lookupTransform("/CameraBottom_frame","/ARUCOFRAME",rospy.Time(0))
    #     print("aruco thingy")
    #     print(trans,rot)
    #     H_aruco_to_camera = tf.transformations.euler_matrix(rot[0],rot[1],rot[2])
    #     H_aruco_to_camera[:3,3] = trans
    
    #     useSensorValues = True
    #     H_camera_to_torso = self.motionProxy.getTransform("CameraBottom",motion.FRAME_TORSO, useSensorValues)
    #     H_aruco_to_torso = np.multiply(H_camera_to_torso, H_aruco_to_camera)
    #     return H_aruco_to_torso    

    # def aruco_position(self):
    #     aruco_coordinate = rospy.Subscriber("aruco_coordinate",String,self.callback)
    #     # aruco_t = n


def main():
    rospy.init_node('move_joints_server', anonymous=True)
    _pose = pose_service()


    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
	main()

