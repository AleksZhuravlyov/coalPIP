import sys
import os
import numpy as np
import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.props import Props


class MathFrame:
    def __init__(s, config_file):
        s.__config = None
        s.config = configparser.ConfigParser()
        s.config.read(config_file)

        s.__props = None
        s.props = Props(config_file)

        s.__grid_block_n = None
        s.grid_block_n = s.__config.get('Numerical', 'grid_block_n')

        s.__theta_perm = None

    @property
    def config(s):
        return s.__config

    @config.setter
    def config(s, config):
        s.__config = config

    @property
    def props(s):
        return s.__props

    @props.setter
    def props(s, props):
        s.__props = props

    @property
    def grid_block_n(s):
        return s.__grid_block_n

    @grid_block_n.setter
    def grid_block_n(s, grid_block_n):
        s.__grid_block_n = int(grid_block_n)

    @property
    def theta_perm(s):
        return s.__theta_perm

    @theta_perm.setter
    def theta_perm(s, theta_perm):
        s.__theta_perm = np.array(theta_perm, dtype=float)

    def __str__(s):
        out_str = str(s.props)
        out_str += '\ngrid_block_n ' + str(s.grid_block_n)
        out_str += '\ntheta_perm ' + str(s.theta_perm)
        return out_str

    def load_txt_theta_perm(s):
        theta_perm_file = str(s.config.get('Matching', 'theta_perm_file'))
        s.theta_perm = np.loadtxt(theta_perm_file, dtype=float)

    def dens(s, press):
        return np.dot(press, s.props.a_dens) + s.props.b_dens

    def density_der(s, press):
        return s.props.a_dens

    def perm(s, press):
        k = np.arange(s.theta_perm.shape[0])
        press_series = np.power.outer(press, k).transpose()
        return np.dot(s.theta_perm, press_series)

    @staticmethod
    def delta_press(press_A, press_B):
        return press_B - press_A


if __name__ == '__main__':
    math_frame = MathFrame(config_file=sys.argv[1])
    math_frame.load_txt_theta_perm()
    print(math_frame)
