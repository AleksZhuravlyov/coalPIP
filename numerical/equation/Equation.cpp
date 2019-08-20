#include <Equation.h>

Equation::Equation(const std::vector<double> &propsVector,
                   const std::vector<std::string> &thetaFiles,
                   const std::vector<double> &_time,
                   const std::vector<double> &_pressIn,
                   const std::vector<double> &_pressOut,
                   const std::vector<double> &_consumption) :
        general(propsVector),
        local(general, thetaFiles),
        convective(general),
        time(_time),
        pressIn(_pressIn),
        pressOut(_pressOut),
        consumption(_consumption) {

    press.emplace_back(std::vector<double>(general.props.gridBlockN, 0));
    press.emplace_back(std::vector<double>(general.props.gridBlockN, 0));

}


std::ostream &operator<<(std::ostream &stream,
                         const Equation &equation) {
    stream << equation.general.props;
    return stream;
}
