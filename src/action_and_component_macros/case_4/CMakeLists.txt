cmake_minimum_required(VERSION 3.12)



###
 add_hpx_component( actions_4 ## SHARED doesn't work here
    SOURCES actions.cpp
    HEADERS actions.hpp
 )
 
## add_library( actions_4 SHARED
##     SOURCES
##     actions.hpp
##     actions.cpp
## )
## 
## hpx_setup_target( actions_4 )



###
add_hpx_executable( case_4
SOURCES
    main.cpp 
    COMPONENT_DEPENDENCIES actions_4
)

## target_link_libraries(case_4 PRIVATE actions_4 )
## 
## hpx_setup_target( case_4 )


