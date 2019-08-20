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


# numerical module

include_directories(
        numerical
        numerical/math
        numerical/equation)

python_add_module(solver
        numerical/SolverWrapper.cpp
        numerical/Solver.cpp
        numerical/Props.cpp
        numerical/math/General.cpp
        numerical/math/Local.cpp
        numerical/math/Convective.cpp
        numerical/equation/Equation.cpp
        numerical/equation/Steady.cpp
        numerical/equation/Transient.cpp)

target_include_directories(solver PUBLIC
        ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})

target_link_libraries(solver ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

set_target_properties(solver PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/../numerical)


# C++ executable

add_executable(main main.cpp)