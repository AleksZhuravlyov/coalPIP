#include <Props.h>

#include <vector>


Props::Props(const std::vector<double> &propsVector) :
        aDens(propsVector[0]),
        bDens(propsVector[1]),
        visc(propsVector[2]),
        length(propsVector[3]),
        area(propsVector[4]),
        gridBlockN(propsVector[5]),
        deltaVolume(propsVector[6]),
        deltaLength(propsVector[7]),
        iterativeAccuracy(propsVector[8]){}


std::ostream &operator<<(std::ostream &stream, const Props &props) {
    stream << "aDens " << props.aDens << std::endl;
    stream << "bDens " << props.bDens << std::endl;
    stream << "visc " << props.visc << std::endl;
    stream << "length " << props.length << std::endl;
    stream << "area " << props.area << std::endl;
    stream << "gridBlockN " << props.gridBlockN << std::endl;
    stream << "deltaVolume " << props.deltaVolume << std::endl;
    stream << "deltaLength " << props.deltaLength << std::endl;
    stream << "iterativeAccuracy " << props.iterativeAccuracy;
    return stream;
}
