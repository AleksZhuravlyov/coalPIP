#include <boost/python.hpp>

#include <Some.h>
#include <PythonConversions.h>

namespace p = boost::python;


BOOST_PYTHON_MODULE (some) {

    providePythonThings();

    p::class_<Some>("SomeWrapper", p::init<>())
            .def(p::init<bool, int, double, std::string,
	                     std::vector<bool>, std::vector<int>,
					     std::vector<double>, std::vector<std::string>>
                         (p::args("var_bool", "var_int", "var_float", "var_str",
						          "var_array_bool", "var_array_int",
								  "var_array_float", "var_array_str")))
									  
            .add_property("var_bool",
                          &Some::getVarBool,
                          &Some::setVarBool)
            .add_property("var_int",
                          &Some::getVarInt,
                          &Some::setVarInt)
            .add_property("var_float",
                          &Some::getVarDouble,
                          &Some::setVarDouble)
            .add_property("var_str",
                          &Some::getVarString,
                          &Some::setVarString)

		    .add_property("var_array_bool",
			              &Some::getVarVectorBool,
			              &Some::setVarVectorBool)
			.add_property("var_array_int",
			              &Some::getVarVectorInt,
			              &Some::setVarVectorInt)
            .add_property("var_array_float",
                          &Some::getVarVectorDouble,
                          &Some::setVarVectorDouble)			
            .add_property("var_array_str",
                          &Some::getVarVectorString,
                          &Some::setVarVectorString)
							  
			.def("say_hi", &Some::sayHi)
			.def("return_hi", &Some::returnHi)
			.def("say_word", &Some::sayWord, p::args("word"))
			.def("return_word", &Some::returnWord, p::args("word"));
}