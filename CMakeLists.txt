# CMakeList.txt : CMake project for hpx_snippets, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.12)

project(hpx_snippets CXX)

# Global Dependencies
find_package(HPX CONFIG REQUIRED)

# programs
add_subdirectory(src)
