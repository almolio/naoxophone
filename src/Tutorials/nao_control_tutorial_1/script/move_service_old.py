#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
import rospy
import time
import almath
import sys

from std_msgs.msg import String
from sensor_msgs.msg import JointState
from naoqi import ALProxy
from nao_control_tutorial_1.srv import MoveJoints, MoveJointsResponse
motionProxy =ALProxy('ALMotion','10.152.246.81', 9559)
import argparse

# def handle_move_service(req):
#     # motionProxy = ALProxy('ALMotion','10.152.246.81', 9559) #81
    

#     # name  = req.name
#     # angle = req.angle*almath.TO_RAD # req.angle
#     # speed = req.speed

#     name  = 'HeadYaw'
#     angle = -0.3 # req.angle
#     speed = 0.5


#     print('Moving joint {} at speed {} and angle {}.'.format(name, speed, angle))
    
#     useSensors    = False
#     commandAngles = motionProxy.getAngles(name, useSensors)
#     print('Returning Angle:', commandAngles[0])

#     motionProxy.setStiffnesses(name, 1.0)
#     fractionMaxSpeed = 0.1
#     motionProxy.setAngles(name,angle,fractionMaxSpeed)
#     # taskList = motionProxy.getTaskList()
#     # print(taskList)
#     # motionProxy.killAll()

#     #motionProxy.killTask(taskList[0][0])
#     # print(taskList)
#     # motionProxy.killTask(taskList[1])
#     motionProxy.setStiffnesses(name, 0.0)

#     useSensors    = False
#     commandAngles = motionProxy.getAngles(name, useSensors)
#     print('Returning Angle:', commandAngles[0])

#     return MoveJointsResponse(commandAngles[0])

# def move_service():

#     rospy.init_node('move_service')
#     # r = rospy.Rate(10)
#     # while(not rospy.is_shutdown()):
#     s = rospy.Service('move_service', MoveJoints, handle_move_service)
#     print('Ready to move.')
#     rospy.spin()

# def timed_interpolation(req):
#     print('Start timed interpolation')
#     # names  = req.name
#     # angleLists = req.angle*almath.TO_RAD # req.angle
#     # times = req.times
#     # isAbsolute =True
#     names = "HeadYaw"
#     angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
#     times      = [1.0,  2.0, 3.0,  4.0, 5.0]
#     isAbsolute = True
#     motionProxy.angleInterpolation(names,angleLists,times,isAbsolute)

# def interpolation_service():
#     rospy.init_node('move_service')
#     # r = rospy.Rate(10)
#     # while(not rospy.is_shutdown()):
#     s = rospy.Service('move_service', MoveJoints, timed_interpolation)
#     print('Ready to move.')
#     rospy.spin()


def handleJointAngles(self, msg):
        rospy.logdebug("Received a joint angle target")
        try:
            # Note: changeAngles() and setAngles() are non-blocking functions.
            if (msg.relative==0):
                self.motionProxy.setAngles(list(msg.joint_names), list(msg.joint_angles), msg.speed)
            else:
                self.motionProxy.changeAngles(list(msg.joint_names), list(msg.joint_angles), msg.speed)
        except RuntimeError,e:
            rospy.logerr("Exception caught:\n%s", e)


if __name__ == '__main__':
    move_service()
    interpolation_service()


