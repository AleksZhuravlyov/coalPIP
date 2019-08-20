#include <Solver.h>

#include <iostream>
#include <iomanip>

Solver::Solver(const std::vector<double> &propsVector,
               const std::vector<std::string> &thetaFiles,
               const std::vector<double> &time,
               const std::vector<double> &pressIn,
               const std::vector<double> &pressOut,
               const std::vector<double> &consumption) :
        transient(propsVector, thetaFiles,
                  time, pressIn, pressOut, consumption) {}


void Solver::print() {
    std::cout << transient << std::endl;
}

void Solver::test() {
    std::cout << "test" << std::endl;

    std::cout << std::setw(17) << std::left << "time";
    for (auto &&element : transient.time)
        std::cout << std::setw(12) << element;
    std::cout << std::endl;
    std::cout << std::setw(17) << std::left << "pressIn";
    for (auto &&element : transient.pressIn)
        std::cout << std::setw(12) << element;
    std::cout << std::endl;
    std::cout << std::setw(17) << std::left << "pressOut";
    for (auto &&element : transient.pressOut)
        std::cout << std::setw(12) << element;
    std::cout << std::endl;
    std::cout << std::setw(17) << std::left << "consumption";
    for (auto &&element : transient.consumption)
        std::cout << std::setw(12) << element;
    std::cout << std::endl;

}
