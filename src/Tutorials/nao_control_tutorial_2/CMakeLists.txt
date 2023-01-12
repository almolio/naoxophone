cmake_minimum_required(VERSION 2.8.3)
project(nao_control_tutorial_2)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  rospy
  message_generation
  sensor_msgs
  cv_bridge
  image_transport
  tf
)

add_service_files(
    DIRECTORY srv
    FILES
    MoveJoints.srv
)

generate_messages(DEPENDENCIES std_msgs)
catkin_package(CATKIN_DEPENDS message_runtime)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS 
		./script/move_service.py 
		./script/client.py
		./script/tfbroadcast.py
    ./script/handtracking.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


find_package(OpenCV REQUIRED)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} /usr/local/lib/cmake)
find_package(aruco REQUIRED)

