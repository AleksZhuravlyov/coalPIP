import sys
import os

import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


if len(sys.argv) == 2:
    ini_file = sys.argv[1]
else:
    ini_file = '../config/config.ini'

config = configparser.ConfigParser()
config.read(ini_file)

for section in config.sections():
    print()
    print('[' + section + ']')
    for key in config[section]:
        print(key, config.get(section, key))


