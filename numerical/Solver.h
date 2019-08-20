#ifndef COALPIP_SOLVER_H
#define COALPIP_SOLVER_H

#include <Props.h>


class Solver {

public:

    Solver(const std::vector<double> &propsVector);

    virtual ~Solver() {}


    Props props;

    void print();


};


#endif //COALPIP_SOLVER_H
