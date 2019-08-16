#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <boost/python.hpp>
#include <boost/python/numpy.hpp>

namespace p = boost::python;
namespace np = boost::python::numpy;


np::ndarray returnArray();
void squareArray(np::ndarray &array);
double sumArray(np::ndarray &array);

#endif //FUNCTIONS_H
