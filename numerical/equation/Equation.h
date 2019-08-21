#ifndef COALPIP_EQUATION_H
#define COALPIP_EQUATION_H

#include <vector>
#include <Eigen/Sparse>

#include <Props.h>
#include <Local.h>
#include <Convective.h>


typedef Eigen::Triplet<double> Triplet;
typedef Eigen::SparseMatrix<double, Eigen::RowMajor> Matrix;
typedef Matrix::InnerIterator MatrixIterator;
typedef Eigen::VectorXd Vector;
typedef Eigen::SparseLU<Eigen::SparseMatrix<double>> SparseLU;


class Equation {

public:

    Equation(const std::vector<double> &propsVector,
             const std::vector<std::string> &thetaFiles,
             const std::vector<double> &_time,
             const std::vector<double> &_pressIn,
             const std::vector<double> &_pressOut,
             const std::vector<double> &_consumptionFact);

    virtual ~Equation() = default;


    friend std::ostream &operator<<(std::ostream &stream,
                                    const Equation &equation);


    void calculateLambda();

    void calculateBeta();

    void calculatePress();

    double calculatePressRelDiff();

    double calculateConsumption();

    virtual void calculateConsumptionSet()  = 0;

    virtual void setTheta(const std::vector<double> &theta)  = 0;

    double calculateEmpiricalRisk(const std::vector<double> &thetaPerm);


    Props props;

    Local local;

    Convective convective;

    int &dim;

    std::vector<double> time;
    std::vector<double> pressIn;
    std::vector<double> pressOut;
    std::vector<double> consumptionFact;

    std::vector<double> consumptionCalc;


    std::vector<std::vector<double>> press;

    int iCurr;
    int iPrev;

    Matrix matrix;

    Vector freeVector;

    Vector variable;

};


#endif //COALPIP_EQUATION_H
