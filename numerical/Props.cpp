#include <Props.h>

#include <vector>


Props::Props(const std::vector<double> &propsVector) : aDens(propsVector[0]),
                                                       bDens(propsVector[1]),
                                                       visc(propsVector[2]),
                                                       length(propsVector[3]),
                                                       area(propsVector[4]) {}


std::ostream &operator<<(std::ostream &stream, const Props &props) {
    stream << "aDens " << props.aDens << std::endl;
    stream << "bDens " << props.bDens << std::endl;
    stream << "visc " << props.visc << std::endl;
    stream << "length " << props.length << std::endl;
    stream << "area " << props.area << std::endl;
    return stream;
}
