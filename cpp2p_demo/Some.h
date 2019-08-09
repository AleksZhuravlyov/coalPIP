#include <string>
#include <vector>
#include <iostream>

class Some {

public:

    Some(const bool &_varBool,
         const int &_varInt,
         const double &_varDouble,
         const std::string &_varString,
		 const std::vector<bool> &_varVectorBool,
		 const std::vector<int> &_varVectorInt,
		 const std::vector<double> &_varVectorDouble,
         const std::vector<std::string> &_varVectorString);

    Some();

    virtual ~Some();	
    
	
	/// accessors and mutators

    bool getVarBool() const;

    void setVarBool(const bool &varBool);
    

    int getVarInt() const;

    void setVarInt(int _varInt);
    

    double getVarDouble() const;

    void setVarDouble(double _varDouble);
    

    std::string getVarString() const;

    void setVarString(const std::string &_varString);
    
	
    std::vector<bool> getVarVectorBool() const;

    void setVarVectorBool(const std::vector<bool> &_varVectorBool);
	
	
    std::vector<int> getVarVectorInt() const;

    void setVarVectorInt(const std::vector<int> &_varVectorInt);
	

    std::vector<double> getVarVectorDouble() const;

    void setVarVectorDouble(const std::vector<double> &_varVectorDouble);
	
	
    std::vector<std::string> getVarVectorString() const;

    void setVarVectorString(const std::vector<std::string> &_varVectorString);
	
	
	/// methods
	
	void sayHi() const;

	std::string returnHi() const;

	void sayWord(const std::string &word) const;

	std::string returnWord(const std::string &word) const;


private:

    bool varBool;

    int varInt;

    double varDouble;

    std::string varString;	

    std::vector<bool> varVectorBool;
	
	std::vector<int> varVectorInt;

    std::vector<double> varVectorDouble;
	
	std::vector<std::string> varVectorString;

};

