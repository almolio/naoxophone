#!/usr/bin/env python2

# SAFETYLIMIT OF THE HEAD 
# PITCH: -0.67  TO 0.5
# YAW: -2.08 TO 2.07

# use rostopic list  .... then rostopic info
# naoqi_bridge_msgs/JointAnglesWithSpeed


# Use: rosmsg show naoqi_bridge_msgs/JointAnglesWithSpeed

# std_msgs/Header header
#   uint32 seq
#   time stamp
#   string frame_id
# string[] joint_names
# float32[] joint_angles
# float32 speed
# uint8 relative



import rospy
from sensor_msgs.msg import JointState
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
import sys
#from control_msgs.msg import FollowJointTrajectoryActionResult
#from control_msgs.msg import FollowJointTrajectoryActionGoal

def callback(data):
    print ("Position pitch: ", data.position[1])
    print ("Position yaw: ", data.position[0])
    

def head_to_home():
    pub = rospy.Publisher('joint_angles', JointAnglesWithSpeed, queue_size=1)
    rospy.init_node('homehead', anonymous=True)
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        home_postition = JointAnglesWithSpeed()

        # Let only push 2 first position see if the head move 
        home_postition.joint_names.append('HeadYaw') #'HeadPitch'
        home_postition.joint_angles.append(0)
        home_postition.joint_names.append('HeadPitch') #'HeadPitch'
        home_postition.joint_angles.append(0)
        home_postition.relative = False
        home_postition.speed = 0.1
        pub.publish(home_postition)
        r.sleep()


if __name__ == '__main__':
    head_to_home()
