cmake_minimum_required(VERSION 2.8.3)
project(nao_control_tutorial_1)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  rospy
  message_generation
  sensor_msgs
  cv_bridge
)

add_service_files(
    DIRECTORY srv
    FILES
    MoveJoints.srv
    InterpolateJoints.srv
)

generate_messages(DEPENDENCIES std_msgs)
catkin_package(CATKIN_DEPENDS message_runtime)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS ./script/move_service.py ./script/interpolate_service.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
add_executable(tut_05 src/client.cpp)

target_link_libraries(tut_05 ${catkin_LIBRARIES})

include_directories(${OpenCV_INCLUDE_DIRS})
find_package(OpenCV REQUIRED)
target_link_libraries(tut_05 ${OpenCV_LIBRARIES})

find_package(aruco REQUIRED)
target_link_libraries(tut_05 ${aruco_LIBS})


