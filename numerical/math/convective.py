import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../'))

from numerical.math.general import General


class Convective:
    def __init__(s, general):
        s.__general = general

        s.delta_length = s.__general.props.length / s.__general.grid_block_n

    def __str__(s):
        out_str = str(s.__general)
        out_str += '\ndelta_length ' + str(s.delta_length)
        return out_str

    @staticmethod
    def left_surf(value):
        value = np.array(value)
        return np.append(value[0], value)

    @staticmethod
    def right_surf(value):
        return np.append(value, value[-1])

    def beta(s, conducty_left, conducty_right):
        conducty_av = (conducty_left + conducty_right) / 2
        return - conducty_av * s.__general.props.area / s.delta_length

    def consumption(s, beta, press_left, press_right):
        return beta * s.__general.delta_press(press_left, press_right)


if __name__ == '__main__':
    general = General(config_file=sys.argv[1])
    convective = Convective(general)
    print(convective)
