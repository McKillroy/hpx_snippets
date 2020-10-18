
cmake_minimum_required(VERSION 3.12)

SET(CMAKE_VERBOSE_MAKEFILE ON)

project(hpx_snippets CXX)

# Dependencies
find_package(HPX CONFIG REQUIRED)

# programs
add_subdirectory(src)

