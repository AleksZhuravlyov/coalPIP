import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from output.plot_optimized_sample import plot_optimized_sample
from analytical.steady_base import SteadyBase


class SteadyAnalytical:
    def __init__(s, config_file, polynomial_degree):
        s.__steady_base = SteadyBase(config_file, polynomial_degree)

    def calculate(s):
        s.__steady_base.calculate_leastsq_problem()
        s.__steady_base.calculate_G_using_theta()
        s.__steady_base.save_theta()
        s.__steady_base.calculate_G_rel_err()

    def plot(s):
        plot_optimized_sample(s.__steady_base,
                              title='Steady State Analytical')


if __name__ == '__main__':
    steady_analytical = SteadyAnalytical(config_file=sys.argv[1],
                                         polynomial_degree=3)
    steady_analytical.calculate()
    steady_analytical.plot()
