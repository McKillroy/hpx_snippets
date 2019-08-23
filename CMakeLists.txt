# CMakeList.txt : CMake project for hpx_snippets, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.12)

project(hpx_snippets CPP)


## Global Dependencies
##
SET(VCPKG_DIR_BASE "F:\\vcpkg\\installed\\x64-windows\\share")

## benchmark


## boost
SET(Boost_Dir "VCPKG_DIR_BASE\\")

## catch2

## hwloc  
SET(HWLOC_DIR  "${VCPKG_DIR_BASE}\\"   )

## hpx
SET(HPX_DIR  "${VCPKG_DIR_BASE}\\hpx"   )
find_package(HPX CONFIG REQUIRED)

## programs
include_directories(src)

