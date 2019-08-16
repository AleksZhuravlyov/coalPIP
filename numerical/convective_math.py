import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.math_frame import MathFrame


class ConvectiveMath:
    def __init__(s, math_frame):
        s.__math_frame = math_frame
        s.math_frame = math_frame

        s.__delta_length = None
        s.delta_length = s.math_frame.props.length / s.math_frame.grid_block_n

    @property
    def math_frame(s):
        return s.__math_frame

    @math_frame.setter
    def math_frame(s, math_frame):
        s.__math_frame = math_frame

    @property
    def delta_length(s):
        return s.__delta_length

    @delta_length.setter
    def delta_length(s, delta_length):
        s.__delta_length = float(delta_length)

    def __str__(s):
        out_str = str(s.math_frame)
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
        return - conducty_av * s.math_frame.props.area / s.delta_length

    def consumption(s, beta, press_left, press_right):
        return beta * s.math_frame.delta_press(press_left, press_right)


if __name__ == '__main__':
    math_frame = MathFrame(config_file=sys.argv[1])
    convective_math = ConvectiveMath(math_frame)
    convective_math.math_frame.load_txt_theta_perm()
    print(convective_math)
