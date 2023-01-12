#!/usr/bin/env python

# SAFETYLIMIT OF THE HEAD 
# PITCH: -0.67  TO 0.5
# YAW: -2.08 TO 2.07


import rospy
from sensor_msgs.msg import JointState
import sys
#from control_msgs.msg import FollowJointTrajectoryActionResult
#from control_msgs.msg import FollowJointTrajectoryActionGoal

def callback(data):
    print ("Position pitch: ", data.position[1])
    print ("Position yaw: ", data.position[0])
    # print('datashape', len(data.position))
    


def joint_subscriber():
    rospy.init_node('joint_subscriber', anonymous=True)
    rospy.Subscriber('joint_states', JointState, callback)
    rospy.spin()



if __name__ == '__main__':
    joint_subscriber()

