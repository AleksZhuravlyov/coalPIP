import sys
import os

import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


class Config:
    def __init__(self, file_name):
        # parameters_file is path and file name for processed lab data.
        self.__parameters_file = None

        self.parse(file_name)

    @property
    def parameters_file(self):
        return self.__parameters_file

    @parameters_file.setter
    def parameters_file(self, parameters_file):
        self.__parameters_file = str(parameters_file)

    def parse(self, file_name):
        parser = configparser.ConfigParser()
        parser.read(file_name)

        self.parameters_file = str(parser.get('Main', 'parameters_file'))

    def __str__(self):
        out_str = '\ncoalPIP config\n'

        out_str += '\nMain:\n'
        out_str += 'parameters_file' + ' = ' + str(self.parameters_file) + '\n'

        return out_str


if __name__ == '__main__':

    if len(sys.argv) == 2:
        ini_file = sys.argv[1]
    else:
        ini_file = '../config/config.ini'

    config = Config(file_name=ini_file)

    print(config)
