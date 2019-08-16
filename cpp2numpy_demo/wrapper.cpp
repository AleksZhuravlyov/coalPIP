#include <functions.h>


BOOST_PYTHON_MODULE (functions) {

    setenv("PYTHONPATH", ".", 1);
    Py_Initialize();
    np::initialize();

    def("return_array", returnArray);
    def("square_array", squareArray, p::args("array"));
    def("sum_array", sumArray, p::args("array"));

}