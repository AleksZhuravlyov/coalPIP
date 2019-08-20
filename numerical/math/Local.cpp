#include <Local.h>

#include <fstream>
#include <cmath>

Local::Local(const General &_general,
             const std::vector<std::string> &thetaFiles) :
        general(_general),
        thetaPermFile(thetaFiles[0]),
        thetaPoroFile(thetaFiles[1]),
        alpha(std::vector<double>(general.props.gridBlockN, 0)),
        lambda(std::vector<double>(general.props.gridBlockN, 0)) {
    loadThetaPerm();
    loadThetaPoro();
}


std::ostream &operator<<(std::ostream &stream, const Local &local) {

    stream << local.general.props;
    stream << "thetaPermFile " << local.thetaPermFile << std::endl;
    stream << "thetaPoroFile " << local.thetaPoroFile << std::endl;

    stream << "thetaPerm";
    for (auto &&element : local.thetaPerm)
        stream << " " << element;
    stream << std::endl;

    stream << "thetaPoro";
    for (auto &&element : local.thetaPoro)
        stream << " " << element;
    stream << std::endl;

    return stream;

}


int Local::left(const int &index) {
    return index;
}

int Local::right(const int &index) {
    return index + 1;
}


std::vector<double> Local::loadTxt(const std::string &fileName) {
    std::ifstream stream;
    stream.open(fileName.c_str());
    std::string word;
    std::vector<double> array;
    while (stream >> word)
        array.push_back(atof(word.c_str()));
    stream.close();
    return array;
}

void Local::loadThetaPerm() {
    thetaPerm = loadTxt(thetaPermFile);
}

void Local::loadThetaPoro() {
    thetaPoro = loadTxt(thetaPoroFile);
}


double Local::perm(const double &press) {
    double value = 0;
    for (int i = 0; i < thetaPerm.size(); i++)
        value += thetaPerm[i] * pow(press, i);
    return value;
}

double Local::poro(const double &press) {
    double value = 0;
    for (int i = 0; i < thetaPoro.size(); i++)
        value += thetaPoro[i] * pow(press, i);
    return value;
}

double Local::poroDer(const double &press) {
    double value = 0;
    for (int i = 1; i < thetaPoro.size(); i++)
        value += thetaPoro[i] * pow(press, (i - 1)) / i;
    return value;
}

void Local::CalculateAlpha(const std::vector<double> &press,
                           const double &dt) {

    for (int i = 0; i < alpha.size(); i++) {
        alpha[i] = poro(press[i]) * general.densDer(press[i]);
        alpha[i] += poroDer(press[i]) * general.dens(press[i]);
        alpha[i] *= general.props.deltaVolume / dt;
    }

}

void Local::CalculateLambda(const std::vector<double> &press) {
    for (int i = 0; i < lambda.size(); i++)
        lambda[i] =
                general.dens(press[i]) * perm(press[i]) / general.props.visc;
}
