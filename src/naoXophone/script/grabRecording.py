#!/usr/bin/env python

import rospy
import sys
from sensor_msgs.msg import JointState
import os 
from naoqi import ALProxy


# docs: http://doc.aldebaran.com/2-4/naoqi/motion/control-joint-api.html 

naoIP = str(os.getenv("NAO_IP"))

class grabSticks:
    def __init__(self):
        self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)

        # GETTING THE ANGLES
        # self.joint_sub = rospy.Subscriber('joint_states', JointState, self.joint_state_callback)
        self.rightarm = ["RShoulderPitch","RShoulderRoll","RElbowYall","RElbowRoll","RWristYall","Rhand"]

        self.joint_squence = []
        

    # def joint_state_callback(self):
# 
        # pass

    def recordJointState(self): 
        pass

    def run(self): 
        # Position the Nao 
        # Let press the Head Button to start joint recording 
        # Write these joint state into a file (So we could update this in the future-- Calibration)    
        # Press again to stop 

        # Reset the state
        # Press another button to Repeat the sequence. 
        pass

##############
# SEND MOVEMENT TO NAO 
##############

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



def main():
    # TODO: ESTABLISH THE JOINT LIMITS? 

    rospy.init_node('grabSticks', anonymous=True)
    nao_grab_stick = grabSticks()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_grab_stick.run()
        rate.sleep()


if __name__ == '__main__':
	main()
