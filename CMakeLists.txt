CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

PROJECT(PoC) # Proof Of Concept
set(CMAKE_CXX_STANDARD 17)

add_subdirectory(file_io)
add_subdirectory(CAN_Messages)

message(STATUS "Generated Include path = ${CAN_INCLUDE_DIR},sources = ${CAN_SOURCES}")

add_subdirectory(main_component)