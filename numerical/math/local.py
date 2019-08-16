import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../'))

from numerical.math.general import General


class Local:
    def __init__(s, general):
        s.__general = general

        s.delta_t = None

        s.delta_volume = s.__general.props.length * s.__general.props.area
        s.delta_volume /= s.__general.grid_block_n

        s.theta_perm = None
        s.theta_poro = None

    def __str__(s):
        out_str = str(s.__general)
        out_str += '\ntheta_perm ' + str(s.theta_perm)
        out_str += '\ntheta_poro ' + str(s.theta_poro)
        out_str += '\ndelta_volume ' + str(s.delta_volume)
        out_str += '\ndelta_t ' + str(s.delta_t)
        return out_str

    def load_txt_theta_perm(s):
        get = s.__general.config.get
        theta_perm_file = str(get('Matching', 'theta_perm_file'))
        s.theta_perm = np.loadtxt(theta_perm_file, dtype=float)

    def load_txt_theta_poro(s):
        get = s.__general.config.get
        theta_poro_file = str(get('Matching', 'theta_poro_file'))
        s.theta_poro = np.loadtxt(theta_poro_file, dtype=float)

    def perm(s, press):
        k = np.arange(s.theta_perm.shape[0])
        press_series = np.power.outer(press, k).transpose()
        return np.dot(s.theta_perm, press_series)

    def poro(s, pressure):
        k = np.arange(s.theta_poro.shape[0])
        pressure_series = np.power.outer(pressure, k).transpose()
        return np.dot(s.theta_poro, pressure_series)

    def poro_der(s, pressure):
        k = np.arange(s.theta_poro.shape[0] - 1)
        pressure_series = np.power.outer(pressure, k).transpose()
        return np.dot(s.theta_poro[1:], pressure_series)

    def alpha(s, pressure):
        value = np.dot(s.poro(pressure), s.__general.density_der(pressure))
        value += np.dot(s.poro_der(pressure), s.__general.dens(pressure))
        value *= s.delta_volume / s.delta_t
        return value

    def conducty(s, pressure):
        dens = s.__general.dens
        perm = s.__general.perm
        visc = s.__general.props.visc
        return dens(pressure) * perm(pressure) / visc


if __name__ == '__main__':
    general = General(config_file=sys.argv[1])
    local = Local(general)
    local.load_txt_theta_perm()
    local.load_txt_theta_poro()
    local.delta_t = 1
    print(local)
