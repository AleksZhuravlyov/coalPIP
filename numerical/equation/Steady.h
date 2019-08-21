#ifndef COALPIP_STEADY_H
#define COALPIP_STEADY_H

#include <Equation.h>


class Steady : public Equation {

public:

    Steady(const std::vector<double> &propsVector,
           const std::vector<std::string> &thetaFiles,
           const std::vector<double> &time,
           const std::vector<double> &pressIn,
           const std::vector<double> &pressOut,
           const std::vector<double> &consumption);

    ~Steady() override = default;

    void calculateLinearPressDistrib(const double &pressIn,
                                     const double &pressOut);

    void calculateSteadyMatrix();

    void calculateSteadyFreeVector(const double &pressIn,
                                   const double &pressOut);




    void runIterativeSteadyProcedure(const double &pressIn,
                                     const double &pressOut);

    void calculateConsumptionSet() final;

    void setTheta(const std::vector<double> &theta) final;


};


#endif //COALPIP_STEADY_H
