import sys
import os
import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


class Properties:
    def __init__(s, config_file):
        s.__config = configparser.ConfigParser()
        s.__config.read(config_file)

        s.__a_dens = None
        s.a_dens = s.__config.get('Properties', 'a_dens')

        s.__b_dens = None
        s.b_dens = s.__config.get('Properties', 'b_dens')

        s.__visc = None
        s.visc = s.__config.get('Properties', 'visc')

        s.__length = None
        s.length = s.__config.get('Properties', 'length')

        s.__cross_sec_area = None
        s.cross_sec_area = s.__config.get('Properties', 'cross_sec_area')

    @property
    def a_dens(s):
        return s.__a_dens

    @a_dens.setter
    def a_dens(s, a_dens):
        s.__a_dens = float(a_dens)

    @property
    def b_dens(s):
        return s.__b_dens

    @b_dens.setter
    def b_dens(s, b_dens):
        s.__b_dens = float(b_dens)

    @property
    def visc(s):
        return s.__visc

    @visc.setter
    def visc(s, visc):
        s.__visc = float(visc)

    @property
    def length(s):
        return s.__length

    @length.setter
    def length(s, length):
        s.__length = float(length)

    @property
    def cross_sec_area(s):
        return s.__cross_sec_area

    @cross_sec_area.setter
    def cross_sec_area(s, cross_sec_area):
        s.__cross_sec_area = float(cross_sec_area)

    def __str__(s):
        out_str = 'a_dens ' + str(s.a_dens)
        out_str += '\nb_dens ' + str(s.b_dens)
        out_str += '\nvisc ' + str(s.visc)
        out_str += '\nlength ' + str(s.length)
        out_str += '\ncross_sec_area ' + str(s.cross_sec_area)
        return out_str


if __name__ == '__main__':
    properties = Properties(config_file=sys.argv[1])
    print(properties)
