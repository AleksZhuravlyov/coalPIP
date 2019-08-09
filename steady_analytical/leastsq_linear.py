import sys
import os
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from steady_analytical.base import Base
from output.plot_steady_result import plot_steady_result


class LeastsqLinear:
    def __init__(s, config_file, polynomial_degree):
        s.__base = Base(config_file, polynomial_degree)
        s.__result = pd.DataFrame(s.__base.parameters.steady.index, dtype=float)

    @property
    def result(s):
        return s.__result

    @result.setter
    def result(s, result):
        s.__result = pd.DataFrame(result)

    def calculate_result(s):
        s.__base.calculate_G_theta_der()
        s.__base.calculate_leastsq_linear()
        s.__base.calculate_G_using_theta_leastsq()
        s.__base.calculate_G_diff_using_theta_leastsq()

        Q_fact = s.__base.G_fact / (s.__base.a_dens * 1.E+5 + s.__base.b_dens)
        s.result['Qoutlet (fact), st. m3/s'] = Q_fact
        Q_calc = s.__base.G_calc / (s.__base.a_dens * 1.E+5 + s.__base.b_dens)
        s.result['Qoutlet (calc), st. m3/s'] = Q_calc
        s.result['Pinlet, Pa'] = s.__base.P_in
        s.result['Poutlet, Pa'] = s.__base.P_out
        s.result['Qdiff'] = s.__base.G_diff
        s.result.index.name = 'time, s'

    def plot_result(s):
        plot_steady_result(s.result, theta=s.__base.theta_leastsq,
                           dens_a=s.__base.a_dens, dens_b=s.__base.b_dens)


if __name__ == '__main__':
    leastsq_linear = LeastsqLinear(config_file=sys.argv[1], polynomial_degree=3)
    leastsq_linear.calculate_result()
    leastsq_linear.plot_result()
