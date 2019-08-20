import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../../'))

from p_numerical.math.general import General
from p_numerical.math.local import Local
from p_numerical.math.convective import Convective


class Equation:
    def __init__(s, config_file):
        s.general = General(config_file)
        s.local = Local(s.general)
        s.convective = Convective(s.general)

    def __str__(s):
        out_str = str(s.local)
        out_str += '\ndelta_length ' + str(s.convective.delta_length)
        return out_str


if __name__ == '__main__':
    equation = Equation(config_file=sys.argv[1])
    print(equation)
