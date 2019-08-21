#ifndef COALPIP_SOLVER_H
#define COALPIP_SOLVER_H

#include <Steady.h>


class Solver {

public:

    Solver(const std::vector<double> &propsVector,
           const std::vector<std::string> &thetaFiles,
           const std::vector<double> &_time,
           const std::vector<double> &_pressIn,
           const std::vector<double> &_pressOut,
           const std::vector<double> &_consumption);

    virtual ~Solver() {}


    Steady steady;

    void print();

    double test(const std::vector<double> &thetaPerm);


};


#endif //COALPIP_SOLVER_H
