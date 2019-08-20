#ifndef COALPIP_CONVECTIVE_H
#define COALPIP_CONVECTIVE_H

#include <General.h>

#include <vector>


class Convective {

public:

    explicit Convective(const General &_general);

    virtual ~Convective() = default;


    friend std::ostream &operator<<(std::ostream &stream,
                                    const Convective &convective);


    static int left(const int &index);

    static int right(const int &index);


    void calculateBeta(const std::vector<double> &lambda);

    double consumption(const std::vector<double> &press);


    General general;

    std::vector<double> beta;


};


#endif //COALPIP_CONVECTIVE_H
