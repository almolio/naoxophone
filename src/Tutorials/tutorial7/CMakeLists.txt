cmake_minimum_required(VERSION 3.0.2)
project(tutorial7)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  message_generation
  roscpp
  rospy
  sensor_msgs
  std_msgs
  tf
  actionlib_msgs
  naoqi_bridge_msgs
)


# catkin_package(
#   INCLUDE_DIRS include
#   LIBRARIES tutorial7
#   CATKIN_DEPENDS cv_bridge image_transport message_generation roscpp rospy sensor_msgs std_msgs tf actionlib_msgs
#   DEPENDS system_lib
# )


# add_service_files(
#     DIRECTORY srv
#     FILES
#     MoveJoints.srv
# )

add_action_files(
  FILES
  blink.action
)


generate_messages(DEPENDENCIES 
                    std_msgs actionlib_msgs
                    )


# catkin_package(CATKIN_DEPENDS message_runtime)
# include_directories(
#   ${catkin_INCLUDE_DIRS}
# )

catkin_install_python(PROGRAMS 
		./script/naoblink.py 
    ./script/naowalk.py 
    ./scriot/naotalk.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


find_package(OpenCV REQUIRED)


find_package(Boost REQUIRED COMPONENTS system thread)
# include_directories(${Boost_INCLUDE_DIRS})
# target_link_libraries(tutorial7 ${Boost_LIBRARIES})