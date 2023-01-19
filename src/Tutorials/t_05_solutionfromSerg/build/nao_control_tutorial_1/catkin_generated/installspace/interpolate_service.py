#!/usr/bin/env python2
import rospy
import time
import almath
import sys
import os
from naoqi import ALProxy
from nao_control_tutorial_1.srv import InterpolateJoints
import json
from std_srvs.srv import Empty
motionProxy = 0
taskID = None
limits = None

def check_limits(req):
    """
    Ensures all requested angles are in the joint limits. See file 'joint_limits_DEG.json'
    """
    global limits
    return req

def send_interpolate_movement(req):
    global taskID
    print(req, type(req.joint_names), type(req.angles), type(req.times))
    req.angles = [a*almath.TO_RAD for a in req.angles]
    names = []
    angles = []
    times = []
    counter = 0
    for i, name in enumerate(req.joint_names):
        names.append(name)
        steps = req.steps[i]
        angles.append(list(req.angles[counter:counter+steps]))
        times.append(list(req.times[counter:counter+steps]))
        counter += steps

    print('names: ', names)
    print('angles: ', angles)
    print('times: ', times)
    
    if(req.blocking):
        motionProxy.angleInterpolation(names, angles, times, not req.relative)
    else:
        motionProxy.post.angleInterpolation(names, angles, times, not req.relative)
        time.sleep(0.5)
        
        taskList = motionProxy.getTaskList()
        print(taskList)
        
        previous_taskID = taskID
        taskID = taskList[0][1]
        if(previous_taskID is not None):
            motionProxy.killTask(previous_taskID)
        
    return True

def interpolate_server():

    print("Interpolate Server started")
    s = rospy.Service('interpolate_server', InterpolateJoints, send_interpolate_movement)


if __name__ == '__main__':
    with open('/home/hrsa/t_05/src/nao_control_tutorial_1/script/joint_limits_DEG.json', 'rb') as f:
        limits = json.load(f)

    robotIP=str(os.getenv("NAO_IP"))
    PORT= 9559
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    rospy.init_node('interpolate_server')
    #TODO init service

    try:
        interpolate_server()
    except rospy.ROSInterruptException:
        rospy.loginfo("ohoh interpolate")


    rospy.spin()
			
		
