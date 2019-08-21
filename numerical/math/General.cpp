#include <General.h>


General::General(const std::vector<double> &propsVector) :
        props(propsVector) {}


std::ostream &operator<<(std::ostream &stream,
                         const General &general) {
    stream << general.props;
    return stream;
}

double General::dens(const double &press) {
    return props.aDens * press + props.bDens;
}

double General::densDer(const double &press) {
    return props.bDens;
}
