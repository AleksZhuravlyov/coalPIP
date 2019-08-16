import sys
import os
import numpy as np
import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.props import Props


class MathFrame:
    def __init__(s, config_file):
        s.config = configparser.ConfigParser()
        s.config.read(config_file)

        s.props = Props(config_file)

        s.grid_block_n = int(s.config.get('Numerical', 'grid_block_n'))

        s.theta_perm = None

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
