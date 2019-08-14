import sys
import os
import numpy as np
from scipy import optimize

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from analytical.steady_base import SteadyBase
from output.plot_optimized_sample import plot_optimized_sample


class SteadyScipy:
    def __init__(s, config_file, polynomial_degree, theta_ini):
        s.__steady_base = SteadyBase(config_file, polynomial_degree)
        s.__theta_ini = np.array(theta_ini, dtype=float)

    def calculate(s):
        optimization = optimize.minimize(s.__steady_base.empirical_risk,
                                         s.__theta_ini, method="Nelder-Mead")
        s.__steady_base.theta = optimization.x
        s.__steady_base.save_theta()
        s.__steady_base.calculate_G_using_theta()
        s.__steady_base.calculate_G_rel_err()

    def plot(s):
        plot_optimized_sample(s.__steady_base, title='Steady State SciPy')


if __name__ == '__main__':
    degree = 1
    ini = np.zeros(degree + 1, dtype=float)
    ini[0] = 1.e-17

    steady_scipy = SteadyScipy(config_file=sys.argv[1],
                               polynomial_degree=degree,
                               theta_ini=ini)
    steady_scipy.calculate()
    steady_scipy.plot()
