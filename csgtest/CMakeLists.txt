
set(INCLUDE_DIR         ${CMAKE_CURRENT_SOURCE_DIR}/include     )
set(SRC_DIR             ${CMAKE_CURRENT_SOURCE_DIR}/src         )



# Locate GTest
find_package(GTest REQUIRED)

set(GTEST_INCLUDE_DIR /usr/include/)
set(SORT_INCLUDE_DIR ${PROJECT_DIR}/sorting/include )




set(INC ${INCLUDE_DIR}/test_sort.hpp

)
set(SRC	${SRC_DIR}/main.cpp
)


message(status "    test SORT_INCLUDE_DIR: " ${SORT_INCLUDE_DIR})

include_directories(${INCLUDE_DIR} ${Boost_INCLUDE_DIRS} ${GTEST_INCLUDE_DIRS} ${GTEST_INCLUDE_DIR} ${SORT_INCLUDE_DIR})


add_executable(csgtests ${SRC} ${INC} ${SORT_INCLUDE_DIR})
target_link_libraries(csgtests ${GTEST_LIBRARIES} pthread)
