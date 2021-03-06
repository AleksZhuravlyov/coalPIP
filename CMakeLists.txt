cmake_minimum_required(VERSION 3.14)

project(coalPIP)

set(CMAKE_CXX_STANDARD 17)

set(PYTHON_LIBRARY "/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/libpython3.8.dylib")
set(PYTHON_INCLUDE_DIR "/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/include/python3.8")
find_package(PythonLibs)

set(Boost_NO_BOOST_CMAKE TRUE)
find_package(Boost REQUIRED COMPONENTS python38 numpy38)

find_package(Eigen3 REQUIRED)


include_directories(
        numerical/equation
        numerical/math
        numerical/utilities)


python_add_module(cfd
        numerical/wrapper.cpp
        numerical/equation/Equation.cpp
        numerical/equation/Steady.cpp
        numerical/equation/Transient.cpp
        numerical/math/Props.cpp
        numerical/math/Local.cpp
        numerical/math/Convective.cpp)


target_include_directories(cfd PUBLIC
        ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS} ${EIGEN3_INCLUDE_DIRS})

target_link_libraries(cfd
        ${Boost_LIBRARIES} ${PYTHON_LIBRARIES} ${EIGEN3_LIBRARIES})

set_target_properties(cfd PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/../numerical)

