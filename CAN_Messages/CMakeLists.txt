execute_process(
        # COMMAND cmd arg1 arg 2 arg ...
        COMMAND "python3" "file_IO.py"
        # working directory -> our folder with CMakeList.txt
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

set(CAN_INCLUDE_DIR
                "${CMAKE_CURRENT_SOURCE_DIR}/output/include"
                PARENT_SCOPE)
set(CAN_SOURCES
            ${CMAKE_CURRENT_SOURCE_DIR}/output/src/min_signals.cpp
            PARENT_SCOPE)

