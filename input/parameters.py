import sys
import os
import pandas as pd
import configparser

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from input.plot_parameters import plot_parameters
from input.parameters_frame import ParametersFrame


class Parameters(ParametersFrame):
    def __init__(s, config_file):
        super().__init__()
        s.__config = configparser.ConfigParser()
        s.__config.read(config_file)

    # Process particular parameters types.

    def process_origin(s):
        parameters_file = str(s.__config.get('Main', 'parameters_file'))
        s.origin = pd.read_csv(parameters_file, index_col='time',
                               parse_dates=True)
        s.origin.index.name = 'time'
        s.origin.columns.name = 'parameters'

    def process_entire(s):
        if s.origin is None:
            s.process_origin()
        s.entire = s.origin.copy()
        s.__data_to_seconds(s.entire)

    def process_steady(s):
        if s.origin is None:
            s.process_origin()
        s.steady = s.origin.copy()
        s.__data_to_seconds(s.steady)
        time_min = float(s.__config.get('Steady', 'time_min'))
        time_max = float(s.__config.get('Steady', 'time_max'))
        s.steady = s.steady[s.steady.index >= time_min]
        s.steady = s.steady[s.steady.index <= time_max]

    def process_transient(s):
        if s.origin is None:
            s.process_origin()
        s.transient = s.origin.copy()
        s.__data_to_seconds(s.transient)
        time_min = float(s.__config.get('Transient', 'time_min'))
        time_max = float(s.__config.get('Transient', 'time_max'))
        s.transient = s.transient[s.transient.index >= time_min]
        s.transient = s.transient[s.transient.index <= time_max]

    def __data_to_seconds(s, data_sample):
        time_series = pd.Series(s.origin.index - s.origin.index[0])
        data_sample.index = time_series.dt.total_seconds()
        data_sample.index.name = 'time, s'

    # Plot particular parameters types.

    def plot_origin(s, y_min=None, y_max=None, y2_min=None, y2_max=None):
        if s.origin is None:
            s.process_origin()
        plot_parameters(s.origin, 'origin', y_min, y_max, y2_min, y2_max)

    def plot_entire(s, y_min=None, y_max=None, y2_min=None, y2_max=None):
        if s.entire is None:
            s.process_entire()
        plot_parameters(s.entire, 'entire', y_min, y_max, y2_min, y2_max)

    def plot_steady(s, y_min=None, y_max=None, y2_min=None, y2_max=None):
        if s.steady is None:
            s.process_steady()
        plot_parameters(s.steady, 'steady', y_min, y_max, y2_min, y2_max)

    def plot_transient(s, y_min=None, y_max=None, y2_min=None, y2_max=None):
        if s.transient is None:
            s.process_transient()
        plot_parameters(s.transient, 'transient', y_min, y_max, y2_min, y2_max)


if __name__ == '__main__':
    parameters = Parameters(config_file=sys.argv[1])
