#include <functions.h>


BOOST_PYTHON_MODULE (functions) {

    setenv("PYTHONPATH", ".", 1);
    Py_Initialize();
    np::initialize();

    p::def("return_array", returnArray);
    p::def("square_array", squareArray, p::args("array"));
    p::def("sum_array", sumArray, p::args("array"));

}