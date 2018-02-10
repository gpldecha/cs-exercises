
set(INCLUDE_DIR         ${CMAKE_CURRENT_SOURCE_DIR}/include     )
set(SRC_DIR             ${CMAKE_CURRENT_SOURCE_DIR}/src         )


set(STL_INC ${INCLUDE_DIR}/stl_examples.h )

set(STL_SRC ${SRC_DIR}/main.cpp  )

include_directories(${INCLUDE_DIR} ${Boost_INCLUDE_DIRS})

add_executable(stl ${STL_SRC} ${STL_INC})
