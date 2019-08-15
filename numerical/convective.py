import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.frame import Frame


class Convective(Frame):
    def __init__(s, config_file):
        super().__init__(config_file)

        s.__delta_length = None
        s.delta_length = s.props.length / s.grid_block_n

        s.__beta = None

    @property
    def delta_length(s):
        return s.__delta_length

    @delta_length.setter
    def delta_length(s, delta_length):
        s.__delta_length = float(delta_length)

    @property
    def beta(s):
        return s.__beta

    @beta.setter
    def beta(s, beta):
        s.__beta = float(beta)

    def __str__(s):
        out_str = super().__str__()
        out_str += '\ndelta_length ' + str(s.delta_length)
        return out_str

    @staticmethod
    def left_surf(value):
        value = np.array(value)
        return np.append(value[0], value)

    @staticmethod
    def right_surf(value):
        return np.append(value, value[-1])

    def calculate_beta(s, conducty_left, conducty_right):
        conducty_av = (conducty_left + conducty_right) / 2
        s.beta = - conducty_av * s.props.area / s.delta_length

    def consumption(s, press_left, press_right):
        return s.beta * s.delta_press(press_left, press_right)


if __name__ == '__main__':
    convective = Convective(config_file=sys.argv[1])
    convective.load_txt_theta_perm()
    print(convective)
