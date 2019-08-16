import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.math_frame import MathFrame
from numerical.convective_math import ConvectiveMath


class SteadyEqFrame:
    def __init__(s, config_file):
        s.__math_frame = None
        s.math_frame = MathFrame(config_file)

        s.__convective_math = None
        s.convective_math = ConvectiveMath(s.math_frame)

    @property
    def math_frame(s):
        return s.__math_frame

    @math_frame.setter
    def math_frame(s, frame):
        s.__math_frame = frame

    @property
    def convective_math(s):
        return s.__convective_math

    @convective_math.setter
    def convective_math(s, convective):
        s.__convective_math = convective

    def __str__(s):        
        out_str = str(s.convective_math)        
        return out_str


if __name__ == '__main__':
    steady_eq_frame = SteadyEqFrame(config_file=sys.argv[1])
    steady_eq_frame.math_frame.load_txt_theta_perm()
    print(steady_eq_frame)
