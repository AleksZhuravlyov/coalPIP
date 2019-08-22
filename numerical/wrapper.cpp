#include <boost/python.hpp>

#include <string>

#include <Equation.h>
#include <Steady.h>
#include <PythonConversions.h>

namespace p = boost::python;


template <class T>
std::string __str__(T const &t) {
    std::stringstream stream;
    stream << t;
    return stream.str();
}

BOOST_PYTHON_MODULE (cfd) {

    providePythonThings();

    p::class_<Steady>("Steady",
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

            .def("__str__", __str__<Steady>)

            .add_property("theta_perm",
                          &Steady::getThetaPerm,
                          &Steady::setThetaPerm)

            .add_property("time",
                          &Steady::getTime,
                          &Steady::setTime)
            .add_property("press_in",
                          &Steady::getPressIn,
                          &Steady::setPressIn)
            .add_property("press_out",
                          &Steady::getPressOut,
                          &Steady::setPressOut)
            .add_property("consumption_fact",
                          &Steady::getConsumptionFact,
                          &Steady::setConsumptionFact)
            .add_property("consumption_calc",
                          &Steady::getConsumptionCalc,
                          &Steady::setConsumptionCalc)
            .add_property("press",
                          &Steady::getPress,
                          &Steady::setPress)


            .def("calculate_consumptions", &Steady::calculateConsumptions)

            .def("calculate_empirical_risk",
                 &Steady::calculateEmpiricalRisk, p::args("theta_perm"));
}