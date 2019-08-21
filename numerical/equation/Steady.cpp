#include <Steady.h>

#include <iostream>


Steady::Steady(const std::vector<double> &propsVector,
               const std::vector<std::string> &thetaFiles,
               const std::vector<double> &time,
               const std::vector<double> &pressIn,
               const std::vector<double> &pressOut,
               const std::vector<double> &consumption) :
        Equation(propsVector, thetaFiles,
                 time, pressIn, pressOut, consumption) {}


void Steady::calculateLinearPressDistrib(const double &pressIn,
                                         const double &pressOut) {
    for (int i = 0; i < dim; i++)
        press[iPrev][i] = pressIn * (dim - 1 - i) / (dim - 1) +
                          pressOut * i / (dim - 1);

}


void Steady::calculateSteadyMatrix() {

    calculateBeta();

    for (int i = 1; i < matrix.outerSize() - 1; ++i) {

        MatrixIterator it(matrix, i);
        double &betaLeft = convective.beta[Local::left(i)];
        double &betaRight = convective.beta[Local::right(i)];

        it.valueRef() = -betaLeft;
        ++it;
        it.valueRef() = betaLeft + betaRight;
        ++it;
        it.valueRef() = -betaRight;

    }

}

void Steady::calculateSteadyFreeVector(const double &pressIn,
                                       const double &pressOut) {
    freeVector[0] = pressIn;
    for (int i = 1; i < dim - 1; i++)
        freeVector[i] = 0;
    freeVector[dim - 1] = pressOut;
}





void Steady::runIterativeSteadyProcedure(const double &_pressIn,
                                         const double &_pressOut) {
    calculateSteadyFreeVector(_pressIn, _pressOut);
    calculateLinearPressDistrib(_pressIn, _pressOut);
    double accuracy = 0;
    do {
        calculateSteadyMatrix();
        calculatePress();
        accuracy = calculatePressRelDiff();
        std::swap(iCurr, iPrev);
    } while (accuracy > props.iterativeAccuracy);

}


void Steady::calculateConsumptionSet() {
    for (int i = 0; i < consumptionFact.size(); i++) {
        runIterativeSteadyProcedure(pressIn[i], pressOut[i]);
        consumptionCalc[i] = calculateConsumption();
    }
}

void Steady::setTheta(const std::vector<double> &theta){
    local.thetaPerm = theta;
}

