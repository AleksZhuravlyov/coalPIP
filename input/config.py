import sys
import os

import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


class ConfigFrame:
    def __init__(s):
        s.__parameters_file = None
        s.__steady_time_min = None
        s.__steady_time_max = None
        s.__transient_time_min = None
        s.__transient_time_max = None

    @property
    def parameters_file(s):
        return s.__parameters_file

    @parameters_file.setter
    def parameters_file(s, parameters_file):
        s.__parameters_file = str(parameters_file)

    @property
    def steady_time_min(s):
        return s.__steady_time_min

    @steady_time_min.setter
    def steady_time_min(s, steady_time_min):
        s.__steady_time_min = float(steady_time_min)

    @property
    def steady_time_max(s):
        return s.__steady_time_max

    @steady_time_max.setter
    def steady_time_max(s, steady_time_max):
        s.__steady_time_max = float(steady_time_max)

    @property
    def transient_time_min(s):
        return s.__transient_time_min

    @transient_time_min.setter
    def transient_time_min(s, transient_time_min):
        s.__transient_time_min = float(transient_time_min)

    @property
    def transient_time_max(s):
        return s.__transient_time_max

    @transient_time_max.setter
    def transient_time_max(s, transient_time_max):
        s.__transient_time_max = float(transient_time_max)


class Config(ConfigFrame):
    def __init__(s, file_name):
        super().__init__()
        s.parse(file_name)

    def parse(s, file_name):
        parser = configparser.ConfigParser()
        parser.read(file_name)
        s.parameters_file = parser.get('Main', 'parameters_file')
        s.steady_time_min = parser.get('Steady', 'time_min')
        s.steady_time_max = parser.get('Steady', 'time_max')
        s.transient_time_min = parser.get('Transient', 'time_min')
        s.transient_time_max = parser.get('Transient', 'time_max')

    def __str__(s):
        out_str = '\ncoalPIP config\n'

        out_str += '\nMain:\n'
        out_str += 'parameters_file' + ' = ' + str(s.parameters_file) + '\n'

        out_str += '\nSteady:\n'
        out_str += 'time_min' + ' = ' + str(s.steady_time_min) + '\n'
        out_str += 'time_max' + ' = ' + str(s.steady_time_max) + '\n'

        out_str += '\nTransient:\n'
        out_str += 'time_min' + ' = ' + str(s.transient_time_min) + '\n'
        out_str += 'time_max' + ' = ' + str(s.transient_time_max) + '\n'

        return out_str


if __name__ == '__main__':

    if len(sys.argv) == 2:
        ini_file = sys.argv[1]
    else:
        ini_file = '../config/config.ini'

    config = Config(file_name=ini_file)

    print(config)
