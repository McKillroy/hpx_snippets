cmake_minimum_required (VERSION 3.12)


add_hpx_executable(simple_main_01
    SOURCES simple_main_01.cpp
    COMPONENT_DEPENDENCIES iostreams)
