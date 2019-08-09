import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from steady_analytical.base_frame import BaseFrame


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

    def calculate_leastsq_linear(s):
        s.F_leastsq = np.dot(s.G_fact, s.G_theta_der)
        s.A_leastsq = np.dot(s.G_theta_der.transpose(), s.G_theta_der)
        s.theta_leastsq = np.linalg.solve(s.A_leastsq, s.F_leastsq)

    def calculate_G_using_theta_leastsq(s):
        s.G_calc = np.dot(s.G_theta_der, s.theta_leastsq)

    def calculate_G_diff_using_theta_leastsq(s):
        s.G_diff = 2 * np.absolute(s.G_calc - s.G_fact)
        s.G_diff /= np.sum(s.G_calc + s.G_fact)


if __name__ == '__main__':
    base = Base(config_file=sys.argv[1], polynomial_degree=3)
