import sys
import os
import numpy as np
from scipy.sparse import dia_matrix

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.steady_eq_frame import SteadyEqFrame


class SteadyEq(SteadyEqFrame):
    def __init__(s, config_file):
        super().__init__(config_file)

    def __str__(s):
        out_str = super().__str__()
        return out_str


if __name__ == '__main__':
    steady_eq = SteadyEq(config_file=sys.argv[1])
    steady_eq.math_frame.load_txt_theta_perm()
    print(steady_eq)
