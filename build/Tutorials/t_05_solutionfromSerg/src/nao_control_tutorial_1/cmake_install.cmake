# Install script for directory: /home/hrsb/MSNE_HRS/catkin_ws/src/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/hrsb/MSNE_HRS/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nao_control_tutorial_1/srv" TYPE FILE FILES
    "/home/hrsb/MSNE_HRS/catkin_ws/src/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/srv/MoveJoints.srv"
    "/home/hrsb/MSNE_HRS/catkin_ws/src/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/srv/InterpolateJoints.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nao_control_tutorial_1/cmake" TYPE FILE FILES "/home/hrsb/MSNE_HRS/catkin_ws/build/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/catkin_generated/installspace/nao_control_tutorial_1-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/hrsb/MSNE_HRS/catkin_ws/devel/include/nao_control_tutorial_1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/hrsb/MSNE_HRS/catkin_ws/devel/share/roseus/ros/nao_control_tutorial_1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/hrsb/MSNE_HRS/catkin_ws/devel/share/common-lisp/ros/nao_control_tutorial_1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/hrsb/MSNE_HRS/catkin_ws/devel/share/gennodejs/ros/nao_control_tutorial_1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/hrsb/MSNE_HRS/catkin_ws/devel/lib/python2.7/dist-packages/nao_control_tutorial_1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/hrsb/MSNE_HRS/catkin_ws/devel/lib/python2.7/dist-packages/nao_control_tutorial_1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/hrsb/MSNE_HRS/catkin_ws/build/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/catkin_generated/installspace/nao_control_tutorial_1.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nao_control_tutorial_1/cmake" TYPE FILE FILES "/home/hrsb/MSNE_HRS/catkin_ws/build/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/catkin_generated/installspace/nao_control_tutorial_1-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nao_control_tutorial_1/cmake" TYPE FILE FILES
    "/home/hrsb/MSNE_HRS/catkin_ws/build/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/catkin_generated/installspace/nao_control_tutorial_1Config.cmake"
    "/home/hrsb/MSNE_HRS/catkin_ws/build/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/catkin_generated/installspace/nao_control_tutorial_1Config-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nao_control_tutorial_1" TYPE FILE FILES "/home/hrsb/MSNE_HRS/catkin_ws/src/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/nao_control_tutorial_1" TYPE PROGRAM FILES "/home/hrsb/MSNE_HRS/catkin_ws/build/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/catkin_generated/installspace/move_service.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/nao_control_tutorial_1" TYPE PROGRAM FILES "/home/hrsb/MSNE_HRS/catkin_ws/build/Tutorials/t_05_solutionfromSerg/src/nao_control_tutorial_1/catkin_generated/installspace/interpolate_service.py")
endif()

