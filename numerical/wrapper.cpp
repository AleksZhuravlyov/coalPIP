#include <boost/python.hpp>

#include <string>

#include <Steady.h>
#include <Transient.h>
#include <PythonConversions.h>

namespace p = boost::python;


template<class T>
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


            .def("calculate_consumptions",
                 &Steady::calculateConsumptions)

            .def("calculate_empirical_risk",
                 &Steady::calculateEmpiricalRisk,
                 p::args("theta_perm"));


    p::class_<Transient>("Transient",
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

            .def("__str__", __str__<Transient>)

            .add_property("theta_perm",
                          &Transient::getThetaPerm,
                          &Transient::setThetaPerm)
            .add_property("theta_poro",
                          &Transient::getThetaPoro,
                          &Transient::setThetaPoro)

            .add_property("time",
                          &Transient::getTime,
                          &Transient::setTime)
            .add_property("press_in",
                          &Transient::getPressIn,
                          &Transient::setPressIn)
            .add_property("press_out",
                          &Transient::getPressOut,
                          &Transient::setPressOut)
            .add_property("consumption_fact",
                          &Transient::getConsumptionFact,
                          &Transient::setConsumptionFact)
            .add_property("consumption_calc",
                          &Transient::getConsumptionCalc,
                          &Transient::setConsumptionCalc)
            .add_property("press",
                          &Transient::getPress,
                          &Transient::setPress)


            .def("calculate_init_press",
                 &Transient::calculateInitPress)

            .def("calculate_matrix",
                 &Transient::calculateMatrix)

            .def("cfd_procedure",
                 &Transient::cfdProcedure)


            .def("calculate_consumptions",
                 &Transient::calculateConsumptions)

            .def("calculate_empirical_risk",
                 &Transient::calculateEmpiricalRisk,
                 p::args("theta_poro"));

}