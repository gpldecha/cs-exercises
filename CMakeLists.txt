cmake_minimum_required(VERSION 2.8.3)
project(cs-exercises)


set(CMAKE_CXX_FLAGS "-O1 -O2 -O3 -std=c++11 -mtune=native -fPIC -Wall -DARMA_BLAS_LONG -fopenmp -Wno-write-strings")        ## Optimize
set(CMAKE_BUILD_TYPE Release                                                                    )
set(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG}"                                          )
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}"                                        )


set(EXECUTABLE_OUTPUT_PATH  ${PROJECT_SOURCE_DIR}/bin                                           )
set(LIBRARY_OUTPUT_PATH     ${PROJECT_SOURCE_DIR}/lib                                           )


set(PROJECT_DIR         ${CMAKE_CURRENT_SOURCE_DIR}                                             )



message(status "    PROJECT_DIR: " ${PROJECT_DIR}                   )
message(status "    CMAKE_INSTALL_PREFIX:" ${CMAKE_INSTALL_PREFIX}  )

#add_subdirectory(trees)
#add_subdirectory(string)
#add_subdirectory(linkedlist)
add_subdirectory(searching)
add_subdirectory(sorting)
add_subdirectory(stl)
add_subdirectory(utils)
add_subdirectory(ipc)
# add_subdirectory(csgtest)
