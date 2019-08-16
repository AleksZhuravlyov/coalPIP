import sys
import os
import numpy as np
from scipy.sparse import dia_matrix

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.transient_eq_frame import TransientEqFrame


class TransientEq(TransientEqFrame):
    def __init__(s, config_file):
        super().__init__(config_file)

    def __str__(s):
        out_str = super().__str__()
        return out_str


if __name__ == '__main__':
    transient_eq = TransientEq(config_file=sys.argv[1])
    transient_eq.math_frame.load_txt_theta_perm()
    transient_eq.local_math.load_txt_theta_poro()
    transient_eq.local_math.delta_t = 1
    print(transient_eq)
