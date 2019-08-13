import sys
import os
import numpy as np
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.structure import Structure


class SteadyBase(Structure):
    def __init__(s, config_file, polynomial_degree):
        super().__init__(config_file, polynomial_degree)
        s.calculate_G_theta_der()

    def calculate_G_theta_der(s):
        k1 = np.arange(s.polynomial_degree + 1) + 1
        k2 = np.arange(s.polynomial_degree + 1) + 2
        diff_press_k1 = np.power.outer(s.P_in, k1) - np.power.outer(s.P_out, k1)
        s.G_theta_der = diff_press_k1 * s.b_dens / k1 / s.length / s.visc
        diff_press_k2 = np.power.outer(s.P_in, k2) - np.power.outer(s.P_out, k2)
        s.G_theta_der += diff_press_k2 * s.a_dens / k2 / s.length / s.visc

    def calculate_leastsq_problem(s):
        s.F_leastsq = np.dot(s.G_fact, s.G_theta_der)
        s.A_leastsq = np.dot(s.G_theta_der.transpose(), s.G_theta_der)
        s.theta = np.linalg.solve(s.A_leastsq, s.F_leastsq)

    def calculate_G_using_theta(s):
        s.G_calc = np.dot(s.G_theta_der, s.theta)

    def calculate_G_rel_err(s):
        s.G_rel_err = np.absolute((s.G_calc.transpose() - s.G_fact) / s.G_fact)
        s.G_rel_err = s.G_rel_err.transpose()

    def clear_theta_path(s):
        s.theta_path.clear()

    def empirical_risk(s, theta):
        s.theta = theta
        s.calculate_G_using_theta()
        s.calculate_G_rel_err()
        s.theta_path.append(theta)
        return s.G_rel_err.mean(axis=0)

    def return_optimized_sample(s):
        optimized_sample = pd.DataFrame(s.parameters.steady.index, dtype=float)
        Q_fact = s.G_fact / (s.a_dens * 1.E+5 + s.b_dens)
        optimized_sample['Qoutlet (fact), st. m3/s'] = Q_fact
        Q_calc = s.G_calc / (s.a_dens * 1.E+5 + s.b_dens)
        optimized_sample['Qoutlet (calc), st. m3/s'] = Q_calc
        optimized_sample['Pinlet, Pa'] = s.P_in
        optimized_sample['Poutlet, Pa'] = s.P_out
        optimized_sample['Gerror'] = s.G_rel_err
        optimized_sample.index.name = 'time, s'
        return optimized_sample


if __name__ == '__main__':
    steady_base = SteadyBase(config_file=sys.argv[1], polynomial_degree=3)
