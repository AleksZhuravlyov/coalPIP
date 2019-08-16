import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.steady_eq_frame import SteadyEqFrame
from numerical.local_math import LocalMath


class TransientEqFrame(SteadyEqFrame):
    def __init__(s, config_file):
        super().__init__(config_file)

        s.__local_math = None
        s.local_math = LocalMath(s.math_frame)

    @property
    def local_math(s):
        return s.__local_math

    @local_math.setter
    def local_math(s, local):
        s.__local_math = local

    def __str__(s):
        out_str = super().__str__()
        out_str += '\n' + str(s.convective_math)
        return out_str


if __name__ == '__main__':
    transient_eq_frame = TransientEqFrame(config_file=sys.argv[1])
    transient_eq_frame.math_frame.load_txt_theta_perm()
    transient_eq_frame.local_math.load_txt_theta_poro()
    print(transient_eq_frame)
