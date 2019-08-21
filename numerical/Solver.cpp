#include <Solver.h>

#include <iostream>
#include <iomanip>

Solver::Solver(const std::vector<double> &propsVector,
               const std::vector<std::string> &thetaFiles,
               const std::vector<double> &time,
               const std::vector<double> &pressIn,
               const std::vector<double> &pressOut,
               const std::vector<double> &consumption) :
        steady(propsVector, thetaFiles,
               time, pressIn, pressOut, consumption) {}


void Solver::print() {
    std::cout << steady << std::endl;
}

double Solver::test(const std::vector<double> &thetaPerm) {
    return steady.calculateEmpiricalRisk(thetaPerm);
}
