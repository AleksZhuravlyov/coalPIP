import sys
import os

import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


class ConfigFrame:
    def __init__(self):
        self.__parameters_file = None
        self.__steady_time_min = None
        self.__steady_time_max = None
        self.__transient_time_min = None
        self.__transient_time_max = None

    @property
    def parameters_file(self):
        return self.__parameters_file

    @parameters_file.setter
    def parameters_file(self, parameters_file):
        self.__parameters_file = str(parameters_file)

    @property
    def steady_time_min(self):
        return self.__steady_time_min

    @steady_time_min.setter
    def steady_time_min(self, steady_time_min):
        self.__steady_time_min = float(steady_time_min)

    @property
    def steady_time_max(self):
        return self.__steady_time_max

    @steady_time_max.setter
    def steady_time_max(self, steady_time_max):
        self.__steady_time_max = float(steady_time_max)

    @property
    def transient_time_min(self):
        return self.__transient_time_min

    @transient_time_min.setter
    def transient_time_min(self, transient_time_min):
        self.__transient_time_min = float(transient_time_min)

    @property
    def transient_time_max(self):
        return self.__transient_time_max

    @transient_time_max.setter
    def transient_time_max(self, transient_time_max):
        self.__transient_time_max = float(transient_time_max)


class Config(ConfigFrame):
    def __init__(self, file_name):
        super().__init__()
        self.parse(file_name)

    def parse(self, file_name):
        parser = configparser.ConfigParser()
        parser.read(file_name)
        self.parameters_file = parser.get('Main', 'parameters_file')
        self.steady_time_min = parser.get('Steady', 'time_min')
        self.steady_time_max = parser.get('Steady', 'time_max')
        self.transient_time_min = parser.get('Transient', 'time_min')
        self.transient_time_max = parser.get('Transient', 'time_max')

    def __str__(self):
        out_str = '\ncoalPIP config\n'

        out_str += '\nMain:\n'
        out_str += 'parameters_file' + ' = ' + str(self.parameters_file) + '\n'

        out_str += '\nSteady:\n'
        out_str += 'time_min' + ' = ' + str(self.steady_time_min) + '\n'
        out_str += 'time_max' + ' = ' + str(self.steady_time_max) + '\n'

        out_str += '\nTransient:\n'
        out_str += 'time_min' + ' = ' + str(self.transient_time_min) + '\n'
        out_str += 'time_max' + ' = ' + str(self.transient_time_max) + '\n'

        return out_str


if __name__ == '__main__':

    if len(sys.argv) == 2:
        ini_file = sys.argv[1]
    else:
        ini_file = '../config/config.ini'

    config = Config(file_name=ini_file)

    print(config)
