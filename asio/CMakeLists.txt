find_package(Boost REQUIRED COMPONENTS system thread regex)

set(ASIO_INCLUDE_DIR         ${CMAKE_CURRENT_SOURCE_DIR}/include     )
set(ASIO_SRC_DIR             ${CMAKE_CURRENT_SOURCE_DIR}/src         )


include_directories(${ASIO_INCLUDE_DIR} ${Boost_INCLUDE_DIRS})

add_executable(asio_example1 src/timer1.cpp )
target_link_libraries(asio_example1 ${Boost_LIBRARY_DIRS} -lboost_system)

add_executable(asio_tcp_example1 src/tcp.cpp )
target_link_libraries(asio_tcp_example1 ${Boost_LIBRARY_DIRS} -lboost_system)
