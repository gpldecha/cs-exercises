
set(INCLUDE_DIR         ${CMAKE_CURRENT_SOURCE_DIR}/include     )
set(SRC_DIR             ${CMAKE_CURRENT_SOURCE_DIR}/src         )


set(INC ${INCLUDE_DIR}/ocado.h)

set(SRC ${SRC_DIR}/main.cpp  )

include_directories(${INCLUDE_DIR} ${Boost_INCLUDE_DIRS})

add_executable(sandbox ${SRC} ${INC})
