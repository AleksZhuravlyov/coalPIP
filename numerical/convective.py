import sys
import os
import configparser
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.frame import Frame


class Convective(Frame):
    def __init__(s, config_file):
        super().__init__(config_file)

        s.__theta_perm = None
        perm_file = str(s.config.get('Matching', 'perm_file'))
        s.theta_perm = np.loadtxt(perm_file, dtype=float)

    @property
    def theta_perm(s):
        return s.__theta_perm

    @theta_perm.setter
    def theta_perm(s, theta_perm):
        s.__theta_perm = np.array(theta_perm, dtype=float)

    def __str__(s):
        out_str = '\nConvective'
        out_str += '\n' + super().__str__()
        out_str += '\ntheta_perm ' + str(s.theta_perm)
        out_str += '\n'
        return out_str


if __name__ == '__main__':
    convective = Convective(config_file=sys.argv[1])
    print(convective)
