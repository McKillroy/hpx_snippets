cmake_minimum_required(VERSION 3.12)


add_hpx_executable( include_test_1 
SOURCES
    include_test_main.cpp 
    include_test.hpp
    include_test2.cpp
)

