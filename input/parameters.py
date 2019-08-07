import sys
import os

import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.config import Config
from input.plot_parameters import plot_parameters


class ParametersFrame:
    def __init__(s):
        s.__origin = None
        s.__entire = None
        s.__steady = None
        s.__transient = None

    @property
    def origin(s):
        return s.__origin

    @origin.setter
    def origin(s, origin):
        s.__origin = pd.DataFrame(origin)

    @property
    def entire(s):
        return s.__entire

    @entire.setter
    def entire(s, entire):
        s.__entire = pd.DataFrame(entire)

    @property
    def steady(s):
        return s.__steady

    @steady.setter
    def steady(s, steady):
        s.__steady = pd.DataFrame(steady)

    @property
    def transient(s):
        return s.__transient

    @transient.setter
    def transient(s, transient):
        s.__transient = pd.DataFrame(transient)


class Parameters(ParametersFrame):
    def __init__(s, config_file):
        super().__init__()
        s.__config = Config(file_name=config_file)

    # Process particular parameters types.

    def process_origin(s):
        s.origin = pd.read_csv(s.__config.parameters_file,
                               index_col='time', parse_dates=True)
        s.origin.index.name = 'time'
        s.origin.columns.name = 'parameters'

    def process_entire(s):
        s.process_origin()
        s.entire = s.origin
        s.__data_to_seconds(s.entire)

    def process_steady(s):
        s.process_origin()
        s.steady = s.origin
        s.__data_to_seconds(s.steady)
        s.steady = s.steady[
            s.steady.index >= s.__config.steady_time_min]
        s.steady = s.steady[
            s.steady.index <= s.__config.steady_time_max]

    def process_transient(s):
        s.process_origin()
        s.transient = s.origin
        s.__data_to_seconds(s.transient)
        s.transient = s.transient[
            s.transient.index >= s.__config.transient_time_min]
        s.transient = s.transient[
            s.transient.index <= s.__config.transient_time_max]

    def __data_to_seconds(s, data_sample):
        time_series = pd.Series(s.origin.index - s.origin.index[0])
        data_sample.index = time_series.dt.total_seconds()
        data_sample.index.name = 'time, s'

    # Plot particular parameters types.

    def plot_origin(s, y_min=None, y_max=None, y2_min=None, y2_max=None):
        plot_parameters(s.origin, 'origin', y_min, y_max, y2_min, y2_max)

    def plot_entire(s, y_min=None, y_max=None, y2_min=None, y2_max=None):
        plot_parameters(s.entire, 'entire', y_min, y_max, y2_min, y2_max)

    def plot_steady(s, y_min=None, y_max=None, y2_min=None, y2_max=None):
        plot_parameters(s.steady, 'steady', y_min, y_max, y2_min, y2_max)

    def plot_transient(s, y_min=None, y_max=None, y2_min=None, y2_max=None):
        plot_parameters(s.transient, 'transient', y_min, y_max, y2_min, y2_max)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        ini_file = sys.argv[1]
    else:
        ini_file = '../config/config.ini'

    parameters = Parameters(config_file=ini_file)
    parameters.process_steady()
    parameters.plot_steady()
