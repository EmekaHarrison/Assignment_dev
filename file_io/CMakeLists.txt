cmake_minimum_required(VERSION 3.10)

project(CI_Assignment CXX)

# tells cmake to search for header files in lib/include folder
include_directories(lib/include)
set(FILE_IO_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/lib/include PARENT_SCOPE)
set(SourcesLib lib/src/project.cpp)
set(SourcesApp app/src/maintest.cpp)

# we are telling to cmake to build a library from source code
add_library(file_io_lib ${SourcesLib})

# it is our poor application
add_executable(CI_Assignment_cmake ${SourcesApp})

# link our library to an executable file
target_link_libraries(CI_Assignment_cmake file_io_lib)

# GOOGLE TEST PART

# include Cmake module to be able to download GoogleTest code.
include(FetchContent)

# Declare git repo and tag to fetch:
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG release-1.12.0
)

# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Download or check that googletest is downloaded:
FetchContent_MakeAvailable(googletest)
