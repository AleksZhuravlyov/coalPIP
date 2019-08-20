#ifndef COALPIP_EQUATION_H
#define COALPIP_EQUATION_H

#include <vector>

#include <General.h>
#include <Local.h>
#include <Convective.h>


class Equation {

public:

    Equation(const std::vector<double> &propsVector,
             const std::vector<std::string> &thetaFiles,
             const std::vector<double> &_time,
             const std::vector<double> &_pressIn,
             const std::vector<double> &_pressOut,
             const std::vector<double> &_consumption);

    virtual ~Equation() = default;


    friend std::ostream &operator<<(std::ostream &stream,
                                    const Equation &equation);


    General general;

    Local local;

    Convective convective;

    std::vector<double> time;
    std::vector<double> pressIn;
    std::vector<double> pressOut;
    std::vector<double> consumption;


    std::vector<std::vector<double>> press;

};


#endif //COALPIP_EQUATION_H
