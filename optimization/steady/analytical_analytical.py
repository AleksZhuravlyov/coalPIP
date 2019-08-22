import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../'))

from output.plot_optimized_sample import plot_optimized_sample
from analytical_steady.model import Model


class AnalyticalAnalytical(Model):
    def __init__(s, config_file, polynomial_degree):
        super().__init__(config_file, polynomial_degree)

    def calculate(s):
        s.calculate_leastsq_problem()
        s.calculate_G_using_theta()
        s.save_theta()
        s.calculate_G_rel_err()

    def plot(s):
        plot_optimized_sample(s,
                              'Analytical Steady State Analytical Optimisation')


if __name__ == '__main__':
    analytical_analytical = AnalyticalAnalytical(config_file=sys.argv[1],
                                                 polynomial_degree=3)
    print(analytical_analytical)
    analytical_analytical.calculate()
    analytical_analytical.plot()
