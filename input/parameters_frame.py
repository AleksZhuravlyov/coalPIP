import sys
import os
import pandas as pd
import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


class ParametersFrame:
    def __init__(s, config_file):
        s.__config = configparser.ConfigParser()
        s.__config.read(config_file)

        s.__parameters_file = None
        s.parameters_file = str(s.__config.get('Main', 'parameters_file'))

        s.__origin = None
        s.__entire = None
        s.__steady = None
        s.__transient = None

    @property
    def config(s):
        return s.__config

    @config.setter
    def config(s, config):
        s.__config = config

    @property
    def parameters_file(s):
        return s.__parameters_file

    @parameters_file.setter
    def parameters_file(s, parameters_file):
        s.__parameters_file = str(parameters_file)

    @property
    def origin(s):
        return s.__origin

    @origin.setter
    def origin(s, origin):
        s.__origin = pd.DataFrame(origin)

    @property
    def entire(s):
        return s.__entire

    @entire.setter
    def entire(s, entire):
        s.__entire = pd.DataFrame(entire)

    @property
    def steady(s):
        return s.__steady

    @steady.setter
    def steady(s, steady):
        s.__steady = pd.DataFrame(steady)

    @property
    def transient(s):
        return s.__transient

    @transient.setter
    def transient(s, transient):
        s.__transient = pd.DataFrame(transient)

    def __str__(s):
        out_str = 'parameters_file ' + str(s.parameters_file)
        return out_str


if __name__ == '__main__':
    parameters_frame = ParametersFrame(config_file=sys.argv[1])
    print(parameters_frame)
