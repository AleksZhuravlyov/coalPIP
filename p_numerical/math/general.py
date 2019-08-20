import sys
import os
import numpy as np
import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../'))

from input.props import Props


class General:
    def __init__(s, config_file):
        s.config = configparser.ConfigParser()
        s.config.read(config_file)

        s.props = Props(config_file)

        s.grid_block_n = int(s.config.get('Properties', 'grid_block_n'))

    def __str__(s):
        out_str = str(s.props)
        out_str += '\ngrid_block_n ' + str(s.grid_block_n)
        return out_str

    def dens(s, press):
        return np.dot(press, s.props.a_dens) + s.props.b_dens

    def density_der(s, press):
        return s.props.a_dens

    @staticmethod
    def delta_press(press_A, press_B):
        return press_B - press_A


if __name__ == '__main__':
    general = General(config_file=sys.argv[1])
    print(general)
