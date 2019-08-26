cmake_minimum_required(VERSION 3.12)



###
add_library( actions_4 SHARED
    actions.hpp
    actions.cpp
)

hpx_setup_target( actions_4 )



###
add_executable( case_4
    main.cpp 
)

target_link_libraries(case_4 PRIVATE actions_4 )

hpx_setup_target( case_4 )


