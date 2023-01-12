# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "nao_control_tutorial_2: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(nao_control_tutorial_2_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv" NAME_WE)
add_custom_target(_nao_control_tutorial_2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "nao_control_tutorial_2" "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(nao_control_tutorial_2
  "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/nao_control_tutorial_2
)

### Generating Module File
_generate_module_cpp(nao_control_tutorial_2
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/nao_control_tutorial_2
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(nao_control_tutorial_2_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(nao_control_tutorial_2_generate_messages nao_control_tutorial_2_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv" NAME_WE)
add_dependencies(nao_control_tutorial_2_generate_messages_cpp _nao_control_tutorial_2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nao_control_tutorial_2_gencpp)
add_dependencies(nao_control_tutorial_2_gencpp nao_control_tutorial_2_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nao_control_tutorial_2_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(nao_control_tutorial_2
  "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/nao_control_tutorial_2
)

### Generating Module File
_generate_module_eus(nao_control_tutorial_2
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/nao_control_tutorial_2
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(nao_control_tutorial_2_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(nao_control_tutorial_2_generate_messages nao_control_tutorial_2_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv" NAME_WE)
add_dependencies(nao_control_tutorial_2_generate_messages_eus _nao_control_tutorial_2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nao_control_tutorial_2_geneus)
add_dependencies(nao_control_tutorial_2_geneus nao_control_tutorial_2_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nao_control_tutorial_2_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(nao_control_tutorial_2
  "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/nao_control_tutorial_2
)

### Generating Module File
_generate_module_lisp(nao_control_tutorial_2
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/nao_control_tutorial_2
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(nao_control_tutorial_2_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(nao_control_tutorial_2_generate_messages nao_control_tutorial_2_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv" NAME_WE)
add_dependencies(nao_control_tutorial_2_generate_messages_lisp _nao_control_tutorial_2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nao_control_tutorial_2_genlisp)
add_dependencies(nao_control_tutorial_2_genlisp nao_control_tutorial_2_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nao_control_tutorial_2_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(nao_control_tutorial_2
  "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/nao_control_tutorial_2
)

### Generating Module File
_generate_module_nodejs(nao_control_tutorial_2
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/nao_control_tutorial_2
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(nao_control_tutorial_2_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(nao_control_tutorial_2_generate_messages nao_control_tutorial_2_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv" NAME_WE)
add_dependencies(nao_control_tutorial_2_generate_messages_nodejs _nao_control_tutorial_2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nao_control_tutorial_2_gennodejs)
add_dependencies(nao_control_tutorial_2_gennodejs nao_control_tutorial_2_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nao_control_tutorial_2_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(nao_control_tutorial_2
  "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nao_control_tutorial_2
)

### Generating Module File
_generate_module_py(nao_control_tutorial_2
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nao_control_tutorial_2
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(nao_control_tutorial_2_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(nao_control_tutorial_2_generate_messages nao_control_tutorial_2_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hrsb/MSNE_HRS/catkin_ws/src/nao_control_tutorial_2/srv/MoveJoints.srv" NAME_WE)
add_dependencies(nao_control_tutorial_2_generate_messages_py _nao_control_tutorial_2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nao_control_tutorial_2_genpy)
add_dependencies(nao_control_tutorial_2_genpy nao_control_tutorial_2_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nao_control_tutorial_2_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/nao_control_tutorial_2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/nao_control_tutorial_2
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(nao_control_tutorial_2_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/nao_control_tutorial_2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/nao_control_tutorial_2
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(nao_control_tutorial_2_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/nao_control_tutorial_2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/nao_control_tutorial_2
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(nao_control_tutorial_2_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/nao_control_tutorial_2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/nao_control_tutorial_2
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(nao_control_tutorial_2_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nao_control_tutorial_2)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nao_control_tutorial_2\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nao_control_tutorial_2
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(nao_control_tutorial_2_generate_messages_py std_msgs_generate_messages_py)
endif()
