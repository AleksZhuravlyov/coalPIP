import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.solver import Solver
from input.props import Props
from input.parameters import Parameters

props = Props(config_file=sys.argv[1])
props_array = props.get_props_array()
theta_files_array = props.get_theta_files_array()

parameters = Parameters(config_file=sys.argv[1])
parameters.process_transient()

time = parameters.transient.index.to_numpy()
press_in = parameters.transient['Pinlet, Pa'].to_numpy()
press_out = parameters.transient['Poutlet, Pa'].to_numpy()
consumption = parameters.transient['Qoutlet, st. m3/s'].copy().to_numpy()
consumption *= props.a_dens * 1.E+5 + props.b_dens

solver = Solver(props_array, theta_files_array,
                time, press_in, press_out, consumption)

solver.print()

solver.test()
