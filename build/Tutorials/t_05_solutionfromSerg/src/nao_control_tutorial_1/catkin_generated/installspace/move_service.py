#!/usr/bin/env python2
import rospy
import time
import almath
import sys
import os
from naoqi import ALProxy
from nao_control_tutorial_1.srv import MoveJoints
import json
from std_srvs.srv import Empty
motionProxy =0;

limits = None

def check_limits(req):
    """
    Ensures all requested angles are in the joint limits. See file 'joint_limits_DEG.json'
    """
    global limits
    lims = limits[req.joint_name]
    if req.angle < lims[0]:
        req.angle = lims[0]
    if req.angle > lims[1]:
        req.angle = lims[1]

    if req.speed > 1.0:
        req.speed = 1.0
    if req.speed < 0:
        req.speed = 0.01

    return req

def send_movement(req):
    print(req, type(req.joint_name), type(req.angle), type(req.speed))

    if(req.relative):
        print("Setting relative position to follow marker")
        cur_angle = motionProxy.getAngles(req.joint_name, False)
        req.angle = cur_angle[0]*almath.TO_DEG + req.angle
    
    req = check_limits(req)
    motionProxy.setAngles(req.joint_name, req.angle*almath.TO_RAD, req.speed)
    print(motionProxy.getTaskList())
#    time.sleep(3.0)

    #disable = rospy.ServiceProxy('body_stiffness/disable', Empty)
    #disable()
    return True

def move_server():
    # rospy.init_node('move_server')
    print("Move Server started")
    s = rospy.Service('move_server', MoveJoints, send_movement)


if __name__ == '__main__':
    with open('/home/hrsb/MSNE_HRS/catkin_ws/src/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/script/joint_limits_DEG.json', 'rb') as f:
        limits = json.load(f)

    robotIP=str(os.getenv("NAO_IP"))
    PORT= 9559
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    rospy.init_node('move_server')
    #TODO init service

    try:
        move_server()
    except rospy.ROSInterruptException:
        rospy.loginfo("ohoh")


    rospy.spin()
			
		
