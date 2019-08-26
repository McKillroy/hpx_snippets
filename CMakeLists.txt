
cmake_minimum_required(VERSION 3.12)

SET(CMAKE_VERBOSE_MAKEFILE ON)

project(hpx_snippets CXX)

# Global Dependencies
SET(HPX_DIR "C:/__A/arc_2017/_INSTALL/hpx/stable/Debug/lib/cmake/HPX")
find_package(HPX CONFIG REQUIRED)

# programs
add_subdirectory(src)

