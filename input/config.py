import sys
import os

import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '.'))


class Config:
    def __init__(self):
        # parameters_file is path and file name for processed lab data.
        self.__parameters_file = None

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
        out_str = '\ncoalPIP settings\n'

        out_str += '\nMain:\n'
        out_str += 'parameters_file' + ' = ' + str(self.parameters_file) + '\n'

        return out_str


if __name__ == '__main__':

    ini_file = '../settings/settings.ini'

    config = Config()

    if len(sys.argv) == 2:
        config.parse(file_name=sys.argv[1])
    else:
        config.parse(file_name=ini_file)

    print(config)
