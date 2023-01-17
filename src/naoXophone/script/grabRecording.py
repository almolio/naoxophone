#!/usr/bin/env python

import rospy
import sys

naoIP = '10.152.246.81' #81

class grabSticks:
    def __init__(self):
        self.motionProxy = ALProxy('ALMotion',naoIP, 9559) 
        self.rate = rospy.Rate(1)
        self.join_squence = 
        
    def recordJointState: 
                
    def run: 
        # Position the Nao 
        # Let press the Head Button to start joint recording 
        # Write these joint state into a file (So we could update this in the future-- Calibration)    
        # Press again to stop 

        # Reset the state
        # Press another button to Repeat the sequence. 

def main():
    rospy.init_node('grabSticks', anonymous=True)
    nao_grab_stick = grabSticks()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown(): 
        # print('looping after run')
        nao_grab_stick.run()
        rate.sleep()


if __name__ == '__main__':
	main()
