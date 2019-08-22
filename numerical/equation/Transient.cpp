#include <Transient.h>

Transient::Transient(const std::vector<double> &propsVector,
                     const std::vector<std::string> &thetaFiles,
                     const std::vector<double> &time,
                     const std::vector<double> &pressIn,
                     const std::vector<double> &pressOut,
                     const std::vector<double> &consumption) :
        Equation(propsVector, thetaFiles,
                 time, pressIn, pressOut, consumption) {
    local.loadThetaPerm();
}


void Transient::setTheta(const std::vector<double> &theta){
    setThetaPoro(theta);
}