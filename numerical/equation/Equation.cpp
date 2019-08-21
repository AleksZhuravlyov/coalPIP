#include <Equation.h>

Equation::Equation(const std::vector<double> &propsVector,
                   const std::vector<std::string> &thetaFiles,
                   const std::vector<double> &_time,
                   const std::vector<double> &_pressIn,
                   const std::vector<double> &_pressOut,
                   const std::vector<double> &_consumptionFact) :
        props(propsVector),
        local(props, thetaFiles),
        convective(props),
        dim(props.gridBlockN),
        time(_time),
        pressIn(_pressIn),
        pressOut(_pressOut),
        consumptionFact(_consumptionFact),
        consumptionCalc(_consumptionFact.size(), 0),
        iCurr(0),
        iPrev(1),
        matrix(dim, dim),
        freeVector(dim),
        variable(dim) {


    press.emplace_back(std::vector<double>(dim, 0));
    press.emplace_back(std::vector<double>(dim, 0));

    std::vector<Triplet> triplets;
    triplets.reserve(3 * dim - 4);
    triplets.emplace_back(0, 0, 1);
    for (int i = 1; i < dim - 1; i++) {
        triplets.emplace_back(i, i - 1);
        triplets.emplace_back(i, i);
        triplets.emplace_back(i, i + 1);
    }
    triplets.emplace_back(dim - 1, dim - 1, 1);
    matrix.setFromTriplets(triplets.begin(), triplets.end());

    for (int i = 0; i < dim; i++) {
        freeVector[i] = 0;
        variable[i] = 0;
    }

}


std::ostream &operator<<(std::ostream &stream,
                         const Equation &equation) {
    stream << equation.props;
    return stream;
}


void Equation::calculateLambda() {
    local.calculateLambda(press[iPrev]);
}

void Equation::calculateBeta() {
    calculateLambda();
    convective.calculateBeta(local.lambda);
}


void Equation::calculatePress() {

    SparseLU sparseLU;

    sparseLU.compute(matrix);
    variable = sparseLU.solve(freeVector);

    for (int i = 0; i < dim; i++)
        press[iCurr][i] = variable[i];

}

double Equation::calculatePressRelDiff() {
    double relDiff = 0;
    for (int i = 0; i < dim; i++)
        relDiff += fabs(press[iCurr][i] - press[iPrev][i]) / press[iCurr][i] /
                   dim;
    return relDiff;
}

double Equation::calculateConsumption() {
    int i = dim - 1;
    return convective.beta[Local::left(i)] *
           (press[iPrev][i] - press[iPrev][i - 1]);
}


double Equation::calculateEmpiricalRisk(const std::vector<double> &theta) {

    setTheta(theta);
    calculateConsumptionSet();

    double empiricalRisk = 0;
    for (int i = 0; i < consumptionFact.size(); i++)
        empiricalRisk += fabs(consumptionFact[i] - consumptionCalc[i]) /
                         consumptionFact[i] / consumptionFact.size();

    return empiricalRisk;

}