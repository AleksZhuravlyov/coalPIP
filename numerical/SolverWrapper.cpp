#include <boost/python.hpp>

#include <Solver.h>
#include <PythonConversions.h>

namespace p = boost::python;


BOOST_PYTHON_MODULE (solver) {

    providePythonThings();

    p::class_<Solver>("Solver",
                      p::init<std::vector<double>,
                              std::vector<std::string>,
                              std::vector<double>,
                              std::vector<double>,
                              std::vector<double>,
                              std::vector<double>>(
                              p::args("props_array",
                                      "theta_files_array",
                                      "time",
                                      "press_in",
                                      "press_out",
                                      "consumption")))
            .def("print", &Solver::print)
            .def("test", &Solver::test);
}