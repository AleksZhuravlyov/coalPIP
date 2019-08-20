import sys
import os
import configparser
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


class Props:
    def __init__(s, config_file):
        s.__config = configparser.ConfigParser()
        s.__config.read(config_file)

        s.a_dens = float(s.__config.get('Properties', 'a_dens'))
        s.b_dens = float(s.__config.get('Properties', 'b_dens'))
        s.visc = float(s.__config.get('Properties', 'visc'))
        s.length = float(s.__config.get('Properties', 'length'))
        s.area = float(s.__config.get('Properties', 'area'))

    def get_props_array(s):
        props_list = list()
        props_list.append(s.a_dens)
        props_list.append(s.b_dens)
        props_list.append(s.visc)
        props_list.append(s.length)
        props_list.append(s.area)

        return np.array(props_list, dtype=float)

    def __str__(s):
        out_str = 'a_dens ' + str(s.a_dens)
        out_str += '\nb_dens ' + str(s.b_dens)
        out_str += '\nvisc ' + str(s.visc)
        out_str += '\nlength ' + str(s.length)
        out_str += '\narea ' + str(s.area)
        return out_str


if __name__ == '__main__':
    props = Props(config_file=sys.argv[1])
    print(props)
