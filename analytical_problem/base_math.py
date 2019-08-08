import sys
import os

import configparser
import numpy as np
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.parameters import Parameters


if __name__ == '__main__':

    if len(sys.argv) == 2:
        ini_file = sys.argv[1]
    else:
        ini_file = '../config/config.ini'

    parameters = Parameters(config_file=ini_file)
    parameters.process_steady()
    config = configparser.ConfigParser()
    config.read(ini_file)

    n_time_points = len(parameters.steady.index)
    a = float(config.get('Properties', 'a_dens'))
    b = float(config.get('Properties', 'b_dens'))
    visc = float(config.get('Properties', 'visc'))
    L = float(config.get('Properties', 'L'))
    P_in = parameters.steady['Pinlet, Pa']
    P_out = parameters.steady['Poutlet, Pa']
    G_fact = parameters.steady['Qoutlet, st. m3/s']

    G_factors = np.zeros((n_time_points, 4), dtype=float)
    for i in range(4):
        G_factors[:, i] = (P_in ** (i + 1) - P_out ** (i + 1)) * b / (i + 1)
    for i in range(1, 4, 1):
        G_factors[:, i] += (P_in ** (i + 2) - P_out ** (i + 2)) * a / (i + 2)
    G_factors /= visc * L
    Free = np.dot(G_fact, G_factors)
    Matr = np.dot(G_factors.transpose(), G_factors)
    theta = np.linalg.solve(Matr, Free)
    G = np.dot(G_factors, theta)

    print('G_factors', G_factors)
    print()
    print('Free', Free)
    print()
    print('Matr', Matr)
    print()
    print('theta', theta)
    print()
    print('G', G)
