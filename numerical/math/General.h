#ifndef COALPIP_GENERAL_H
#define COALPIP_GENERAL_H

#include <vector>

#include <Props.h>


class General {

public:

    explicit General(const std::vector<double> &propsVector);

    virtual ~General() = default;


    friend std::ostream &operator<<(std::ostream &stream,
                                    const General &general);


    double dens(const double &press);

    double densDer(const double &press);

    static double deltaPress(const double &pressA, const double &pressB);


    Props props;

};


#endif //COALPIP_GENERAL_H
