cmake_minimum_required(VERSION 3.12)

add_executable( case_3
    main.cpp 
    actions.hpp
    actions.cpp
)

hpx_setup_target( case_3 )

