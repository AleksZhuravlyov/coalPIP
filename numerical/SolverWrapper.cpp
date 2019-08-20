#include <boost/python.hpp>

#include <Solver.h>
#include <PythonConversions.h>

namespace p = boost::python;


BOOST_PYTHON_MODULE (solver) {

    providePythonThings();

    p::class_<Solver>("Solver",
                      p::init<std::vector<double>>(p::args("props_array")))
            .def("print", &Solver::print);
}