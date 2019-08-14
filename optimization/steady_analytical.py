import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from output.plot_optimized_sample import plot_optimized_sample
from analytical_steady.base import Base


class SteadyAnalytical(Base):
    def __init__(s, config_file, polynomial_degree):
        super().__init__(config_file, polynomial_degree)

    def calculate(s):
        s.calculate_leastsq_problem()
        s.calculate_G_using_theta()
        s.save_theta()
        s.calculate_G_rel_err()

    def plot(s):
        plot_optimized_sample(s, title='Steady State Analytical')


if __name__ == '__main__':
    steady_analytical = SteadyAnalytical(config_file=sys.argv[1],
                                         polynomial_degree=3)
    print(steady_analytical)
    steady_analytical.calculate()
    steady_analytical.plot()
