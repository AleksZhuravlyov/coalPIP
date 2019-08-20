#include <Solver.h>

#include <iostream>

Solver::Solver(const std::vector<double> &propsVector) : props(propsVector) {}


void Solver::print() {
    std::cout << props << std::endl;
}