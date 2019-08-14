import sys
import os
import configparser
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.frame import Frame


class Local(Frame):
    def __init__(s, config_file, theta_poro):
        super().__init__(config_file)

        s.__theta_poro = None
        s.theta_poro = theta_poro

    @property
    def theta_poro(s):
        return s.__theta_poro

    @theta_poro.setter
    def theta_poro(s, theta_poro):
        s.__theta_poro = np.array(theta_poro, dtype=float)

    def __str__(s):
        out_str = '\nLocal'
        out_str += '\n' + super().__str__()
        out_str += '\ntheta_poro ' + str(s.theta_poro)
        out_str += '\n'
        return out_str


if __name__ == '__main__':
    local = Local(config_file=sys.argv[1], theta_poro=[0, 1, 2, 3])
    print(local)
