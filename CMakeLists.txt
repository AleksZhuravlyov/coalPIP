cmake_minimum_required(VERSION 3.14)
project(coalPIP)

set(CMAKE_CXX_STANDARD 17)

include_directories(.)
include_directories(leastsq)
include_directories(conversations)

find_package(PythonLibs 3.7 REQUIRED)

find_package(Boost COMPONENTS python37 numpy37 REQUIRED)

set(Some "some")

python_add_module(${Some} leastsq/Some.cpp leastsq/SomeWrapper.cpp)

target_include_directories(${Some} PUBLIC ${Boost_INCLUDE_DIRS}
        ${PYTHON_INCLUDE_DIRS})

target_link_libraries(${Some} ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

set_target_properties(${Some} PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/../leastsq)

add_executable(main main.cpp)