# CMakeList.txt : CMake project for hpx_snippets, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.12)

project(hpx_snippets CXX)

# Global Dependencies
SET(HPX_DIR "C:/__A/arc_2017/_INSTALL/hpx/stable/Debug/lib/cmake/HPX")
find_package(HPX CONFIG REQUIRED)

# programs
add_subdirectory(src)
