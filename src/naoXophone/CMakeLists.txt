cmake_minimum_required(VERSION 3.0.2)
project(naoXophone)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  actionlib_msgs
  cv_bridge
  image_transport
  message_generation
  naoqi_bridge_msgs
  roscpp
  rospy
  sensor_msgs
  std_msgs
  tf
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES naoXophone
#  CATKIN_DEPENDS actionlib_msgs cv_bridge image_transport message_generation naoqi_bridge_msgs roscpp rospy sensor_msgs std_msgs tf
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS 
		script/detectNotes.py
    script/detectNotes2.py
    script/grabRecording.py
		script/notePositions.py
		script/playNotes.py
    script/visual_detection.py
    script/arucoBroadcast.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

