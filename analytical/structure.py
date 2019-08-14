import sys
import os
import configparser
import numpy as np
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.parameters import Parameters
from input.properties import Properties


class Structure:
    def __init__(s, config_file, polynomial_degree):
        s.__parameters = Parameters(config_file)
        s.parameters.process_steady()

        s.__config = configparser.ConfigParser()
        s.__config.read(config_file)

        s.__polynomial_degree = int(polynomial_degree)
        s.__n_time_points = len(s.__parameters.steady.index)

        s.__properties = None
        s.properties = Properties(config_file)

        Q_fact = np.array(s.parameters.steady['Qoutlet, st. m3/s'])
        s.__G_fact = Q_fact
        s.__G_fact *= s.properties.a_dens * 1.E+5 + s.properties.b_dens
        s.__G_theta_der = None
        s.__A_leastsq = None
        s.__F_leastsq = None
        s.__theta = None
        s.__theta_path = list()

        s.__perm_file = None
        s.perm_file = s.__config.get('Matching', 'perm_file')

        s.__G_calc = None
        s.__G_rel_err = None

    @property
    def parameters(s):
        return s.__parameters

    @parameters.setter
    def parameters(s, parameters):
        s.__parameters = pd.DataFrame(parameters)

    @property
    def polynomial_degree(s):
        return s.__polynomial_degree

    @polynomial_degree.setter
    def polynomial_degree(s, polynomial_degree):
        s.__polynomial_degree = int(polynomial_degree)

    @property
    def n_time_points(s):
        return s.__n_time_points

    @n_time_points.setter
    def n_time_points(s, n_time_points):
        s.__n_time_points = int(n_time_points)

    @property
    def properties(s):
        return s.__properties

    @properties.setter
    def properties(s, properties):
        s.__properties = properties

    @property
    def G_fact(s):
        return s.__G_fact

    @G_fact.setter
    def G_fact(s, G_fact):
        s.__G_fact = np.array(G_fact, dtype=float)

    @property
    def G_theta_der(s):
        return s.__G_theta_der

    @G_theta_der.setter
    def G_theta_der(s, G_theta_der):
        s.__G_theta_der = np.array(G_theta_der, dtype=float)

    @property
    def A_leastsq(s):
        return s.__A_leastsq

    @A_leastsq.setter
    def A_leastsq(s, A_leastsq):
        s.__A_leastsq = np.array(A_leastsq, dtype=float)

    @property
    def F_leastsq(s):
        return s.__F_leastsq

    @F_leastsq.setter
    def F_leastsq(s, F_leastsq):
        s.__F_leastsq = np.array(F_leastsq, dtype=float)

    @property
    def theta(s):
        return s.__theta

    @theta.setter
    def theta(s, theta):
        s.__theta = theta

    @property
    def theta_path(s):
        return s.__theta_path

    @theta_path.setter
    def theta_path(s, theta_path):
        s.__theta_path = theta_path

    @property
    def perm_file(s):
        return s.__perm_file

    @perm_file.setter
    def perm_file(s, perm_file):
        s.__perm_file = str(perm_file)

    @property
    def G_calc(s):
        return s.__G_calc

    @G_calc.setter
    def G_calc(s, G_calc):
        s.__G_calc = G_calc

    @property
    def G_rel_err(s):
        return s.__G_rel_err

    @G_rel_err.setter
    def G_rel_err(s, G_rel_err):
        s.__G_rel_err = G_rel_err
