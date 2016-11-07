
set(INCLUDE_DIR         ${CMAKE_CURRENT_SOURCE_DIR}/include     )
set(SRC_DIR             ${CMAKE_CURRENT_SOURCE_DIR}/src         )


set(TREE_INC ${INCLUDE_DIR}/bstree.h )

set(TREE_SRC ${SRC_DIR}/main.cpp  )

include_directories(${INCLUDE_DIR} ${Boost_INCLUDE_DIRS})

add_executable(tree ${TREE_SRC} ${TREE_INC})
