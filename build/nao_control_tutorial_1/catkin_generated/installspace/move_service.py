#!/usr/bin/env python2
# -*- encoding: UTF-8 -*-
import rospy
import almath
from naoqi import ALProxy
from nao_control_tutorial_1.srv import jointAngle, jointAngleResponse, timedInterpolation,  timedInterpolationResponse
#motionProxy =ALProxy('ALMotion','10.152.246.81', 9559)


class move_service():
    def __init__(self):

        self.motionProxy = ALProxy('ALMotion','10.152.246.81', 9559)

        self.rate = rospy.Rate(1)
        
        #Start Services
        self.jointAngleSrv = rospy.Service("jointAngle", jointAngle, self.handle_jointAngle)
        self.timedInterpolationSrv = rospy.Service("timedInterpolation", timedInterpolation, self.handle_timedInterpolation)

        
        # rospy.Subscriber("joint_angles", JointAnglesWithSpeed, self.handle_jointAngle, queue_size=10)
        # #rospy.Subscriber("joint_stiffness", JointState, self.handleJointStiffness, queue_size=10)
        
    
    def handle_jointAngle(self, req):
        print('Angle of Head Pitch is limited to from 3.0 to -3.0. Reason is likely ther robot itself')
        print("Received a joint angle target")
        # self.motionProxy.wakeUp()
        name  = req.name
        angle = req.angle*almath.TO_RAD # req.angle
        speed = req.speed
        useSensors    = False
        print('Angle Recieve {}'.format(angle))
        # commandAngles = self.motionProxy.getAngles(name, useSensors)
        # print('Current Angle:', commandAngles[0])
        self.motionProxy.setStiffnesses(name, 1.0)
        self.rate.sleep()
        self.motionProxy.setAngles(name,angle,speed)
        self.rate.sleep()
        # self.motionProxy.setStiffnesses(name, 0.0)
        # self.rate.sleep()
        commandAngles = self.motionProxy.getAngles(name, useSensors)
        # self.rate.sleep()
        print('Returning Angle:', commandAngles[0])
        # self.motionProxy.rest()
        return jointAngleResponse(commandAngles[0])

    def handle_timedInterpolation(self, req):
        print('Start timed interpolation')
        names  = req.names
        # names    = ["HeadYaw", "HeadPitch"]
        angleLists = req.angleLists#*almath.TO_RAD # req.angle
        angleLists = angleLists.split(' ')
        times = req.times
        times = times.split(' ')
        for i in range(len(times)):
            times[i]      = float(times[i])
            angleLists[i] = float(angleLists[i])
        print('angles',  angleLists)
        print('times:',  times)
        isAbsolute =True
        # names = "HeadYaw"
        # angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
        # times      = [1.0,  2.0, 3.0,  4.0, 5.0]
        # isAbsolute = True
        useSensors    = False
        commandAngles = self.motionProxy.getAngles(names, useSensors)
        print('Current Angle:', commandAngles[0])
        self.motionProxy.setStiffnesses(names, 1.0)
        self.rate.sleep()
        self.motionProxy.angleInterpolation(names,angleLists,times,isAbsolute)
        self.rate.sleep()
        # taskList = self.motionProxy.getTaskList()
        # self.motionProxy.killTask(taskList[0][1])
        self.motionProxy.killAll()
        self.rate.sleep()
        self.motionProxy.setStiffnesses(names, 0.0)
        self.rate.sleep()
        commandAngles = self.motionProxy.getAngles(names, useSensors)
        print('Returning Angle:', commandAngles[0])
        return timedInterpolationResponse(commandAngles[0])

# def main(args):
#     s  = rospy.init_node('move_service', anonymous=True)
#     ic = move_service()

#     type = str(args[1])
#     if type == "normal":
#         service = s.jointAngleSrv
#     elif type == "interpolation":
#         service = s.timedInterpolationSrv
#     try:
#         rospy.spin()
#     except KeyboardInterrupt:
#         print("Shutting down")

def main():
    s  = rospy.init_node('move_service', anonymous=True)
    ic = move_service()

    # service1 = ic.jointAngleSrv
    # service2 = ic.timedInterpolationSrv
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
	main()







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


# def handleJointAngles(self, msg):
#         rospy.logdebug("Received a joint angle target")
#         try:
#             # Note: changeAngles() and setAngles() are non-blocking functions.
#             if (msg.relative==0):
#                 self.motionProxy.setAngles(list(msg.joint_names), list(msg.joint_angles), msg.speed)
#             else:
#                 self.motionProxy.changeAngles(list(msg.joint_names), list(msg.joint_angles), msg.speed)
#         except RuntimeError,e:
#             rospy.logerr("Exception caught:\n%s", e)


# if __name__ == '__main__':
#     move_service()
#     interpolation_service()


