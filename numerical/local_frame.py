import sys
import os
import configparser
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.properties import Properties


class LocalFrame:
    def __init__(s, config_file):
        s.__config = configparser.ConfigParser()
        s.__config.read(config_file)

        s.__properties = None
        s.properties = Properties(config_file)

        s.__grid_block_n = None
        s.grid_block_n = s.__config.get('Numerical', 'grid_block_n')

        s.__theta_perm = None
        perm_file = str(s.__config.get('Matching', 'perm_file'))
        s.theta_perm = np.loadtxt(perm_file, dtype=float)

    @property
    def properties(s):
        return s.__properties

    @properties.setter
    def properties(s, properties):
        s.__properties = properties

    @property
    def grid_block_n(s):
        return s.__grid_block_n

    @grid_block_n.setter
    def grid_block_n(s, grid_block_n):
        s.__grid_block_n = int(grid_block_n)

    @property
    def theta_perm(s):
        return s.__theta_perm

    @theta_perm.setter
    def theta_perm(s, theta_perm):
        s.__theta_perm = np.array(theta_perm, dtype=float)

    def __str__(s):
        out_str = '\nLocalFrame'
        out_str += '\n' + str(s.properties)
        out_str += '\ngrid_block_n ' + str(s.grid_block_n)
        out_str += '\ntheta_perm ' + str(s.theta_perm)
        out_str += '\n'
        return out_str


if __name__ == '__main__':
    local_fame = LocalFrame(config_file=sys.argv[1])
    print(local_fame)
