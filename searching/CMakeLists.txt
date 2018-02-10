
set(SEARCH_INCLUDE_DIR         ${CMAKE_CURRENT_SOURCE_DIR}/include     )
set(SEARCH_SRC_DIR             ${CMAKE_CURRENT_SOURCE_DIR}/src         )


set(INC ${SEARCH_INCLUDE_DIR}/bst.h)


include_directories(${SEARCH_INCLUDE_DIR} ${Boost_INCLUDE_DIRS})

add_executable(bst_example ${SEARCH_SRC_DIR}/bst_example.cpp)
