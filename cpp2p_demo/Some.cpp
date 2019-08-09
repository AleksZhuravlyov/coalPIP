#include <iostream>
#include <string>

#include <Some.h>


Some::Some(const bool &_varBool,
           const int &_varInt,
           const double &_varDouble,
           const std::string &_varString,
		   const std::vector<bool> &_varVectorBool,
		   const std::vector<int> &_varVectorInt,
		   const std::vector<double> &_varVectorDouble,
           const std::vector<std::string> &_varVectorString) :
        varBool(_varBool),
        varInt(_varInt),
        varDouble(_varDouble),
        varString(_varString),
		varVectorBool(_varVectorBool),
		varVectorInt(_varVectorInt),
		varVectorDouble(_varVectorDouble),
        varVectorString(_varVectorString) {}

Some::Some() : Some(bool(),
                    int(),
                    double(),
                    std::string(),
					std::vector<bool>({bool()}),
					std::vector<int>({int()}),
					std::vector<double>({double()}),
                    std::vector<std::string>({std::string()})) {}

Some::~Some() {}


bool Some::getVarBool() const {
    return varBool;
}

void Some::setVarBool(const bool &_varBool) {
    varBool = _varBool;
}


int Some::getVarInt() const {
    return varInt;
}

void Some::setVarInt(int _varInt) {
    varInt = _varInt;
}


double Some::getVarDouble() const {
    return varDouble;
}

void Some::setVarDouble(double _varDouble) {
    varDouble = _varDouble;
}


std::string Some::getVarString() const {
    return varString;
}

void Some::setVarString(const std::string &_varString) {
    varString = _varString;
}


std::vector<bool> Some::getVarVectorBool() const {
    return varVectorBool;
}

void Some::setVarVectorBool(const std::vector<bool> &_varVectorBool) {
    varVectorBool = _varVectorBool;
}


std::vector<int> Some::getVarVectorInt() const {
    return varVectorInt;
}

void Some::setVarVectorInt(const std::vector<int> &_varVectorInt) {
    varVectorInt = _varVectorInt;
}


std::vector<double> Some::getVarVectorDouble() const {
    return varVectorDouble;
}

void Some::setVarVectorDouble(const std::vector<double> &_varVectorDouble) {
    varVectorDouble = _varVectorDouble;
}


std::vector<std::string> Some::getVarVectorString() const {
    return varVectorString;
}

void Some::setVarVectorString(const std::vector<std::string> &_varVectorString) {
    varVectorString = _varVectorString;
}


void Some::sayHi() const {
	std::cout << "Hi" << std::endl;
}

std::string Some::returnHi() const {
	return "Hi";
}

void Some::sayWord(const std::string &word) const {
	std::cout << word << std::endl;
}

std::string Some::returnWord(const std::string &word) const {
	return word;
}
