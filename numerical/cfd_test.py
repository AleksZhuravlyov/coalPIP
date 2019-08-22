import sys
import os
import numpy as np
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical import Steady, Transient
from input import Props, Parameters

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

# steady = Steady(props_array, theta_files_array,
#                 time, press_in, press_out, consumption)
#
# print(steady)
#
# theta_perm = np.loadtxt(props.theta_perm_file, dtype=float)
#
# empirical_risk = steady.calculate_empirical_risk(theta_perm)
#
# print('empirical_risk', empirical_risk)
#
transient = Transient(props_array, theta_files_array,
                      time, press_in, press_out, consumption)

press_in = transient.press_in

press_out = transient.press_out

transient.calculate_init_press()
press_ini = transient.press

transient.cfd_procedure(press_in[0] * 0.95, press_out[0])
press_09 = transient.press

df = pd.DataFrame({'press_ini': press_ini, 'press_095': press_09})

df.plot()
