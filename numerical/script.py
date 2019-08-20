import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from numerical.solver import Solver
from input.props import Props

props = Props(config_file=sys.argv[1])

solver = Solver(props.get_props_array())

solver.print()
