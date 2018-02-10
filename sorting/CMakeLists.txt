
set(SORT_INCLUDE_DIR         ${CMAKE_CURRENT_SOURCE_DIR}/include     )
set(SORT_SRC_DIR             ${CMAKE_CURRENT_SOURCE_DIR}/src         )


set(INC ${SORT_INCLUDE_DIR}/insertion_sort.h
        ${SORT_INCLUDE_DIR}/merge_sort.h
        ${SORT_INCLUDE_DIR}/quick_sort.h
)
set(SRC ${SORT_SRC_DIR}/main.cpp
)


include_directories(${SORT_INCLUDE_DIR} ${Boost_INCLUDE_DIRS})

add_executable(sorting ${SRC} ${INC})
