# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "api_move: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iapi_move:/home/atv-remote/movements/src/api_move/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(api_move_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/atv-remote/movements/src/api_move/msg/movement.msg" NAME_WE)
add_custom_target(_api_move_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "api_move" "/home/atv-remote/movements/src/api_move/msg/movement.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(api_move
  "/home/atv-remote/movements/src/api_move/msg/movement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/api_move
)

### Generating Services

### Generating Module File
_generate_module_cpp(api_move
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/api_move
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(api_move_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(api_move_generate_messages api_move_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/atv-remote/movements/src/api_move/msg/movement.msg" NAME_WE)
add_dependencies(api_move_generate_messages_cpp _api_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(api_move_gencpp)
add_dependencies(api_move_gencpp api_move_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS api_move_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(api_move
  "/home/atv-remote/movements/src/api_move/msg/movement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/api_move
)

### Generating Services

### Generating Module File
_generate_module_eus(api_move
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/api_move
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(api_move_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(api_move_generate_messages api_move_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/atv-remote/movements/src/api_move/msg/movement.msg" NAME_WE)
add_dependencies(api_move_generate_messages_eus _api_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(api_move_geneus)
add_dependencies(api_move_geneus api_move_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS api_move_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(api_move
  "/home/atv-remote/movements/src/api_move/msg/movement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/api_move
)

### Generating Services

### Generating Module File
_generate_module_lisp(api_move
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/api_move
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(api_move_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(api_move_generate_messages api_move_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/atv-remote/movements/src/api_move/msg/movement.msg" NAME_WE)
add_dependencies(api_move_generate_messages_lisp _api_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(api_move_genlisp)
add_dependencies(api_move_genlisp api_move_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS api_move_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(api_move
  "/home/atv-remote/movements/src/api_move/msg/movement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/api_move
)

### Generating Services

### Generating Module File
_generate_module_nodejs(api_move
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/api_move
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(api_move_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(api_move_generate_messages api_move_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/atv-remote/movements/src/api_move/msg/movement.msg" NAME_WE)
add_dependencies(api_move_generate_messages_nodejs _api_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(api_move_gennodejs)
add_dependencies(api_move_gennodejs api_move_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS api_move_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(api_move
  "/home/atv-remote/movements/src/api_move/msg/movement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/api_move
)

### Generating Services

### Generating Module File
_generate_module_py(api_move
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/api_move
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(api_move_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(api_move_generate_messages api_move_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/atv-remote/movements/src/api_move/msg/movement.msg" NAME_WE)
add_dependencies(api_move_generate_messages_py _api_move_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(api_move_genpy)
add_dependencies(api_move_genpy api_move_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS api_move_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/api_move)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/api_move
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(api_move_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/api_move)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/api_move
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(api_move_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/api_move)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/api_move
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(api_move_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/api_move)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/api_move
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(api_move_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/api_move)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/api_move\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/api_move
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(api_move_generate_messages_py std_msgs_generate_messages_py)
endif()
