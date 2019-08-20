#ifndef COALPIP_PROPS_H
#define COALPIP_PROPS_H

#include <vector>
#include <iostream>

class Props {

public:

    explicit Props(const std::vector<double> &propsVector);

    virtual ~Props() {}


    friend std::ostream &operator<<(std::ostream &stream, const Props &props);

    double aDens;
    double bDens;
    double visc;
    double length;
    double area;
    double gridBlockN;
    double deltaVolume;
    double deltaLength;

};


#endif //COALPIP_PROPS_H
