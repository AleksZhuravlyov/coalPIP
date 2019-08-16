import sys
import os
import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


class ParametersFrame:
    def __init__(s, config_file):
        s.config = configparser.ConfigParser()
        s.config.read(config_file)

        s.parameters_file = str(s.config.get('Main', 'parameters_file'))

        s.origin = None
        s.entire = None
        s.steady = None
        s.transient = None

    def __str__(s):
        out_str = 'parameters_file ' + str(s.parameters_file)
        return out_str


if __name__ == '__main__':
    parameters_frame = ParametersFrame(config_file=sys.argv[1])
    print(parameters_frame)
