import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.math_frame import MathFrame


class LocalMath:
    def __init__(s, math_frame):
        s.__math_frame = math_frame
        s.math_frame = math_frame

        s.__theta_poro = None
        s.__delta_t = None

        s.__delta_volume = None
        s.delta_volume = s.math_frame.props.length * s.math_frame.props.area
        s.delta_volume /= s.math_frame.grid_block_n

    @property
    def math_frame(s):
        return s.__math_frame

    @math_frame.setter
    def math_frame(s, frame):
        s.__math_frame = frame

    @property
    def theta_poro(s):
        return s.__theta_poro

    @theta_poro.setter
    def theta_poro(s, theta_poro):
        s.__theta_poro = np.array(theta_poro, dtype=float)

    @property
    def delta_t(s):
        return s.__delta_t

    @delta_t.setter
    def delta_t(s, delta_t):
        s.__delta_t = float(delta_t)

    @property
    def delta_volume(s):
        return s.__delta_volume

    @delta_volume.setter
    def delta_volume(s, delta_volume):
        s.__delta_volume = float(delta_volume)

    def load_txt_theta_poro(s):
        get = s.math_frame.config.get
        theta_poro_file = str(get('Matching', 'theta_poro_file'))
        s.theta_poro = np.loadtxt(theta_poro_file, dtype=float)

    def __str__(s):
        out_str = str(s.math_frame)
        out_str += '\ntheta_poro ' + str(s.theta_poro)
        out_str += '\ndelta_volume ' + str(s.delta_volume)
        return out_str

    def poro(s, pressure):
        k = np.arange(s.theta_poro.shape[0])
        pressure_series = np.power.outer(pressure, k).transpose()
        return np.dot(s.theta_poro, pressure_series)

    def poro_der(s, pressure):
        k = np.arange(s.theta_poro.shape[0] - 1)
        pressure_series = np.power.outer(pressure, k).transpose()
        return np.dot(s.theta_poro[1:], pressure_series)

    def alpha(s, pressure):
        value = np.dot(s.poro(pressure), s.math_frame.density_der(pressure))
        value += np.dot(s.poro_der(pressure), s.math_frame.dens(pressure))
        value *= s.delta_volume / s.delta_t
        return value

    def conducty(s, pressure):
        dens = s.math_frame.dens
        perm = s.math_frame.perm
        visc = s.math_frame.props.visc
        return dens(pressure) * perm(pressure) / visc


if __name__ == '__main__':
    math_frame = MathFrame(config_file=sys.argv[1])
    local_math = LocalMath(math_frame)
    local_math.math_frame.load_txt_theta_perm()
    local_math.load_txt_theta_poro()
    local_math.delta_t = 1
    print(local_math)
