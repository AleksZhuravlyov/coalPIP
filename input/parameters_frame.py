import sys
import os
import pandas as pd

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


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
