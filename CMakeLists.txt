cmake_minimum_required(VERSION 3.14)

project(coalPIP)

set(CMAKE_CXX_STANDARD 17)


# include directories

include_directories(.)
include_directories(cpp2p_demo)
include_directories(cpp2numpy_demo)
include_directories(utilities)


# pakages

find_package(PythonLibs 3.7 REQUIRED)
find_package(Boost COMPONENTS python37 numpy37 REQUIRED)


# some demo module

python_add_module(some
        cpp2p_demo/Some.cpp cpp2p_demo/SomeWrapper.cpp)

target_include_directories(some PUBLIC
        ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})

target_link_libraries(some ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

set_target_properties(some PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/../cpp2p_demo)


# functions demo module

python_add_module(functions
        cpp2numpy_demo/functions.cpp cpp2numpy_demo/wrapper.cpp)

target_include_directories(functions PUBLIC
        ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})

target_link_libraries(functions ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

set_target_properties(functions PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/../cpp2numpy_demo)


# C++ executable

add_executable(main main.cpp)