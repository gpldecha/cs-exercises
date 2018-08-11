set(CMAKE_BUILD_TYPE Release)

add_executable(consumer ${CMAKE_CURRENT_SOURCE_DIR}/src/consumer.cpp)
add_executable(producer ${CMAKE_CURRENT_SOURCE_DIR}/src/producer.cpp)

target_link_libraries(consumer -lrt)
target_link_libraries(producer -lrt)

set_target_properties(consumer
    PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin"
)

set_target_properties(producer
    PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin"
)


find_package( PythonInterp 2.7 REQUIRED )
find_package( PythonLibs 2.7 REQUIRED )

include_directories(/usr/include/python2.7)
find_package(Boost COMPONENTS python REQUIRED)

message(STATUS "PYTHON_LIBRARIES:   ${PYTHON_LIBRARIES}")
message(STATUS "PYTHON_INCLUDE_DIR: ${PYTHON_INCLUDE_DIR}")

add_library(pyipc MODULE ${CMAKE_CURRENT_SOURCE_DIR}/src/pyipc.cpp)
target_link_libraries(pyipc -lrt ${Boost_LIBRARIES} /usr/lib/x86_64-linux-gnu/libpython2.7.so
)

# don't prepend wrapper library name with lib
set_target_properties(pyipc PROPERTIES PREFIX "")

set_target_properties(pyipc
    PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/lib"
)
