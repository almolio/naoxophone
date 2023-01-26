#!/usr/bin/env python
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

def check_limits(name, angle_list):
    """
    Ensures all requested angles are in the joint limits. See file 'joint_limits_DEG.json'
    """
    global limits
    lims = limits[name]
    angles_limited = []
    for angle in angle_list:
        if angle < lims[0]:
            angle = lims[0]
        elif angle > lims[1]:
            angle = lims[1]
        angles_limited.append(angle)
    print("Cleaned angles", angles_limited, ":))))))")
    return angles_limited

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
        if req.relative:
            cur_angle = motionProxy.getAngles(name, False)
            print(cur_angle)
            req_angles = list(req.angles[counter:counter+steps])
            req_angles = [a + cur_angle[0] for a in req_angles]
            req_angles = check_limits(name, list(req.angles[counter:counter+steps]))
            print("hi", req_angles)
            angles.append(req_angles)
        else:
            req.angles = list(req.angles[counter:counter+steps])
        times.append(list(req.times[counter:counter+steps]))
        counter += steps

    print('names: ', names)
    print('angles: ', angles)
    print('times: ', times)
    
    if(req.blocking):
        motionProxy.angleInterpolation(names, angles, times, not req.relative)
    else:
        
        motionProxy.post.angleInterpolation(names, angles, times, True)
        #time.sleep(0.3)
        
        taskList = motionProxy.getTaskList()
        print(taskList)
        
        previous_taskID = taskID
        #taskID = taskList[0][1]
        for num, a in enumerate(taskList):
            if a[0] == 'angleInterpolation':
                taskID = a[1]
                print(taskID)
                break
            else:
                taskID = None

        if(previous_taskID is not None):
            motionProxy.killTask(previous_taskID)
        
    return True

def interpolate_server():

    print("Interpolate Server started")
    s = rospy.Service('interpolate_server', InterpolateJoints, send_interpolate_movement)


if __name__ == '__main__':
    with open('/home/hrsb/MSNE_HRS/catkin_ws/src/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/script/joint_limits_DEG.json', 'rb') as f:
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
			
		
