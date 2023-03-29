set(SOURCES src/main.cpp)

include_directories(${CAN_INCLUDE_DIR})
include_directories(${FILE_IO_INCLUDE_DIR})

add_executable(main_component ${SOURCES} ${CAN_SOURCES})

target_link_libraries(main_component file_io_lib)