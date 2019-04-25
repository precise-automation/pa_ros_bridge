cmake_minimum_required(VERSION 2.8.3)
project(pa_tcs_bridge)



find_package(
  catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_service_files(
  FILES
  TCSService.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  DEPENDS message_runtime
  std_msgs
)

install(PROGRAMS
  scripts/Setup.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)