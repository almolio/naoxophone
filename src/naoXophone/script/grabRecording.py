#!/usr/bin/env python

import rospy
import sys
from sensor_msgs.msg import JointState
import os 
import qi
import argparse
from naoqi import ALProxy
from naoqi_bridge_msgs.msg import HeadTouch

# docs: http://doc.aldebaran.com/2-4/naoqi/motion/control-joint-api.html 

naoIP = str(os.getenv("NAO_IP"))

class grabSticks:
    def __init__(self):
        self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)

        # GETTING THE ANGLES
        # self.joint_sub = rospy.Subscriber('joint_states', JointState, self.joint_state_callback)
        self.head_sub = rospy.Subscriber("/tactile_touch", HeadTouch, self.headtouch_callback)
        self.rightarm = ["RShoulderPitch","RShoulderRoll","RElbowYall","RElbowRoll","RWristYall","Rhand"]
        self.leftarm = ["LShoulderPitch","LShoulderRoll","LElbowYall","LElbowRoll","LWristYall","Lhand"]
        self.botharms = [*self.rightarm, *self.leftarm]
        self.joint_sequence_start = motionProxy.getAngles(names=self.rightarm, useSensors=True)
        print("Initial Position Recorded")
        print("Place the hand on the joystick and press head button")
        self.joint_sequence_end = []
        self.headtouch = HeadTouch(0,0) # Init Headtouch message as empty


    def headtouch_callback(self, headtouch):
        self.headtouch = headtouch   

    def run(self): 
        # Position the Nao 
        # Let press the Head Button to start joint recording 
        if self.headtouch.button is 1 and self.headtouch.state is 1:
            self.joint_sequence_end = motionProxy.getAngles(names=self.botharms, useSensors=True)
            print("Hand and joystick is recorded.")
        # Write these joint state into a file (So we could update this in the future-- Calibration)    

        # Reset the state
        # Press another button to Repeat the sequence. 
        if self.headtouch.button is 2 and self.headtouch.state is 1: 
            self.send_movement(self.joint_sequence_start)
            self.send_movement(self.joint_sequence_end)

        # self.rate.sleep()

##############
# SEND MOVEMENT TO NAO 
##############

    def send_movement(self,position,stay_stiff=True):
        self.motionProxy.setstiffnesses(self.botharms, [1.0 for i in self.botharms])
        fractionMaxSpeed = 0.2
        self.motionProxy.setAngles(self.botharms, position, fractionMaxSpeed)

        if not stay_stiff: 
            self.motionProxy.setstiffnesses(self.botharms, [0.0 for i in self.botharms])

        # print(req, type(req.joint_name), type(req.angle), type(req.speed))

        # if(req.relative):
        #     print("Setting relative position to follow marker")
        #     cur_angle = motionProxy.getAngles(req.joint_name, False)
        #     req.angle = cur_angle[0]*almath.TO_DEG + req.angle
        
        # req = check_limits(req)
        # motionProxy.setAngles(req.joint_name, req.angle*almath.TO_RAD, req.speed)
        # print(motionProxy.getTaskList())
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
