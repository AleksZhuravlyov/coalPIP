import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical import Steady
from input import Props
from input import Parameters

props = Props(config_file=sys.argv[1])
props_array = props.get_props_array()
theta_files_array = props.get_theta_files_array()

parameters = Parameters(config_file=sys.argv[1])
parameters.process_steady()

time = parameters.steady.index.to_numpy()
press_in = parameters.steady['Pinlet, Pa'].to_numpy()
press_out = parameters.steady['Poutlet, Pa'].to_numpy()
consumption = parameters.steady['Qoutlet, st. m3/s'].copy().to_numpy()
consumption *= props.a_dens * 1.E+5 + props.b_dens

steady = Steady(props_array, theta_files_array,
                time, press_in, press_out, consumption)

print(steady)

theta_perm = np.loadtxt(props.theta_perm_file, dtype=float)

empirical_risk = steady.calculate_empirical_risk(theta_perm)

print('empirical_risk', empirical_risk)
