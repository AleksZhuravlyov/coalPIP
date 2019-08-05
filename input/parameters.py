import sys
import os

import matplotlib.pyplot as plt
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.config import Config
from input.plot_parameters import plot_parameters


class Parameters:
    def __init__(self, config_file):
        self.__origin = None
        self.__entire = None
        self.__steady = None
        self.__transient = None

        self.config = Config(file_name=config_file)

    # Accessors and mutators for particular parameters types.

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin):
        self.__origin = pd.DataFrame(origin)

    @property
    def entire(self):
        return self.__entire

    @entire.setter
    def entire(self, entire):
        self.__entire = pd.DataFrame(entire)

    @property
    def steady(self):
        return self.__steady

    @steady.setter
    def steady(self, steady):
        self.__steady = pd.DataFrame(steady)

    @property
    def transient(self):
        return self.__transient

    @transient.setter
    def transient(self, transient):
        self.__transient = pd.DataFrame(transient)

    # Process particular parameters types.

    def process_origin(self):
        self.origin = pd.read_csv(self.config.parameters_file, index_col='time',
                                  parse_dates=True)
        self.origin.index.name = 'time'
        self.origin.columns.name = 'parameters'

    def process_entire(self):
        self.process_origin()
        self.entire = self.origin
        time_series = pd.Series(self.entire.index - self.entire.index[0])
        self.entire.index = time_series.dt.total_seconds()
        self.entire.index.name = 'time, s'

    def process_steady(self):
        pass

    def process_transient(self):
        pass

    # Plot particular parameters types.

    def plot_origin(self, y_min=None, y_max=None, y2_min=None, y2_max=None):
        plot_parameters(self.origin, 'origin', y_min, y_max, y2_min, y2_max)

    def plot_entire(self, y_min=None, y_max=None, y2_min=None, y2_max=None):
        plot_parameters(self.entire, 'entire', y_min, y_max, y2_min, y2_max)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        ini_file = sys.argv[1]
    else:
        ini_file = '../config/config.ini'

    parameters = Parameters(config_file=ini_file)
    parameters.process_entire()
    parameters.plot_entire()
