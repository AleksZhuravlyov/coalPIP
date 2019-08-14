import sys
import os
import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.properties import Properties


class Frame:
    def __init__(s, config_file):
        s.__config = configparser.ConfigParser()
        s.__config.read(config_file)

        s.__properties = None
        s.properties = Properties(config_file)

        s.__grid_block_n = None
        s.grid_block_n = s.__config.get('Numerical', 'grid_block_n')

    @property
    def config(s):
        return s.__config

    @config.setter
    def config(s, config):
        s.__config = config

    @property
    def properties(s):
        return s.__properties

    @properties.setter
    def properties(s, properties):
        s.__properties = properties

    @property
    def grid_block_n(s):
        return s.__grid_block_n

    @grid_block_n.setter
    def grid_block_n(s, grid_block_n):
        s.__grid_block_n = int(grid_block_n)

    def __str__(s):
        out_str = str(s.properties)
        out_str += '\ngrid_block_n ' + str(s.grid_block_n)
        return out_str


if __name__ == '__main__':
    frame = Frame(config_file=sys.argv[1])
    print(frame)
