import sys
import os

import numpy as np
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from steady_analytical_math.base_frame import BaseFrame

from output.plot_steady_result import plot_steady_result


class Base(BaseFrame):
    def __init__(s, config_file, polynomial_degree):
        super().__init__(config_file, polynomial_degree)

    def calculate_G_theta_der(s):
        k1 = np.arange(s.polynomial_degree + 1) + 1
        k2 = np.arange(s.polynomial_degree + 1) + 2
        diff_press_k1 = np.power.outer(s.P_in, k1) - np.power.outer(s.P_out, k1)
        s.G_theta_der = diff_press_k1 * s.b_dens / k1 / s.length / s.visc
        diff_press_k2 = np.power.outer(s.P_in, k2) - np.power.outer(s.P_out, k2)
        s.G_theta_der += diff_press_k2 * s.a_dens / k2 / s.length / s.visc

    def calculate_leastsq_linear_alg(s):
        s.F_leastsq = np.dot(s.G_fact, s.G_theta_der)
        s.A_leastsq = np.dot(s.G_theta_der.transpose(), s.G_theta_der)
        s.theta_leastsq = np.linalg.solve(s.A_leastsq, s.F_leastsq)

    def calculate_G_using_theta_leastsq(s):
        s.G_calc = np.dot(s.G_theta_der, s.theta_leastsq)

    def calculate_G_diff_using_theta_leastsq(s):
        s.G_diff = 2 * np.absolute(s.G_calc - s.G_fact)
        s.G_diff /= np.sum(s.G_calc + s.G_fact)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        ini_file = sys.argv[1]
    else:
        ini_file = '../config/config.ini'

    base = Base(ini_file, polynomial_degree=3)
    base.calculate_G_theta_der()
    base.calculate_leastsq_linear_alg()
    base.calculate_G_using_theta_leastsq()
    base.calculate_G_diff_using_theta_leastsq()

    steady_result = pd.DataFrame(base.parameters.steady.index, dtype=float)
    Q_fact = base.G_fact / (base.a_dens * 1.E+5 + base.b_dens)
    steady_result['Qoutlet (fact), st. m3/s'] = Q_fact
    Q_calc = base.G_calc / (base.a_dens * 1.E+5 + base.b_dens)
    steady_result['Qoutlet (calc), st. m3/s'] = Q_calc
    steady_result['Pinlet, Pa'] = base.P_in
    steady_result['Poutlet, Pa'] = base.P_out
    steady_result['Qdiff'] = base.G_diff
    steady_result.index.name = 'time, s'

    plot_steady_result(steady_result, theta=base.theta_leastsq,
                       dens_a=base.a_dens, dens_b=base.b_dens)
