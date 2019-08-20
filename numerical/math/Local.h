#ifndef COALPIP_LOCAL_H
#define COALPIP_LOCAL_H

#include <General.h>

#include <string>


class Local {

public:

    explicit Local(const General &_general,
                   const std::vector<std::string> &thetaFiles);

    virtual ~Local() = default;


    friend std::ostream &operator<<(std::ostream &stream, const Local &local);


    static int left(const int &index);

    static int right(const int &index);


    std::vector<double> loadTxt(const std::string &fileName);

    void loadThetaPerm();

    void loadThetaPoro();


    double perm(const double &press);

    double poro(const double &press);

    double poroDer(const double &press);

    void CalculateAlpha(const std::vector<double> &press,
                        const double &dt);

    void CalculateLambda(const std::vector<double> &press);


    General general;

    std::string thetaPermFile;
    std::string thetaPoroFile;

    std::vector<double> thetaPerm;
    std::vector<double> thetaPoro;

    std::vector<double> alpha;
    std::vector<double> lambda;

};


#endif //COALPIP_LOCAL_H