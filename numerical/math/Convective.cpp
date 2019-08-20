#include <Convective.h>

#include <General.h>

Convective::Convective(const General &_general) :
        general(_general),
        beta(std::vector<double>(general.props.gridBlockN + 1, 0)) {}


std::ostream &operator<<(std::ostream &stream,
                         const Convective &convective) {
    stream << convective.general.props;
    return stream;
}


int Convective::left(const int &index) {
    return index - 1;
}

int Convective::right(const int &index) {
    return index;
}


void Convective::calculateBeta(const std::vector<double> &lambda) {
    for (int i = 1; i < beta.size() - 1; i++) {
        beta[i] = -(lambda[left(i)] + lambda[right(i)]) / 2;
        beta[i] *= general.props.area / general.props.deltaLength;
    }
}

double Convective::consumption(const std::vector<double> &press) {
    auto index = beta.size() - 2;
    return beta[index] *
           General::deltaPress(press[right(index)], press[right(index)]);
}