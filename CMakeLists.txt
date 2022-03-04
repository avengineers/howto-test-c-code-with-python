# cmake project definition
cmake_minimum_required(VERSION 3.22.0)

set(CMAKE_C_COMPILER clang CACHE STRING "C Compiler")
project(pt1 C)

set(PT1_SWIG_OUT pt1_wrap.c)
add_custom_command(
    OUTPUT ${PT1_SWIG_OUT}
    COMMAND swig -outcurrentdir -python ${CMAKE_CURRENT_LIST_DIR}/src/main/pt1.swig
    DEPENDS ${CMAKE_CURRENT_LIST_DIR}/src/main/pt1.swig ${CMAKE_CURRENT_LIST_DIR}/src/main/pt1.h
)

add_library(
    ${PROJECT_NAME}
    SHARED
    src/main/pt1.c
    ${PT1_SWIG_OUT}
)

set_target_properties(
    ${PROJECT_NAME}
    PROPERTIES
    PREFIX ""
    OUTPUT_NAME "_pt1"
    SUFFIX ".pyd"
)

target_include_directories(
    ${PROJECT_NAME}
    PRIVATE
    src/main
    $ENV{USERPROFILE}/scoop/apps/python/current/include
)

target_link_libraries(
    ${PROJECT_NAME}
    -L$ENV{USERPROFILE}/scoop/apps/python/current/libs
    Python310
)
