import sys
import os

import configparser
import numpy as np
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.parameters import Parameters

from output.plot_steady_result import plot_steady_result

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
    G_fact = parameters.steady['Qoutlet, st. m3/s'] * (a * 1.E+5 + b)

    polynomial_degree = 3

    k1 = np.arange(polynomial_degree + 1) + 1
    k2 = np.arange(polynomial_degree + 1) + 2
    G_factors = (np.power.outer(P_in, k1) - np.power.outer(P_out, k1)) * b / k1
    G_factors += (np.power.outer(P_in, k2) - np.power.outer(P_out, k2)) * a / k2
    G_factors /= L * visc

    F_leastsq = np.dot(G_fact, G_factors)
    A_leastsq = np.dot(G_factors.transpose(), G_factors)
    X_leastsq = np.linalg.solve(A_leastsq, F_leastsq)

    G_calc = np.dot(G_factors, X_leastsq)

    G_diff = 2 * np.absolute(G_calc - G_fact)/np.sum(G_calc + G_fact)

    steady_result = pd.DataFrame(index=parameters.steady.index, dtype=float)
    steady_result['Qoutlet (fact), st. m3/s'] = G_fact / (a * 1.E+5 + b)
    steady_result['Qoutlet (calc), st. m3/s'] = G_calc / (a * 1.E+5 + b)
    steady_result['Pinlet, Pa'] = P_in
    steady_result['Poutlet, Pa'] = P_out
    steady_result['Qdiff'] = G_diff

    plot_steady_result(steady_result, theta=X_leastsq, dens_a=a, dens_b=b)
