import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from  cpp2numpy_demo.functions import return_array, square_array, sum_array

returned_array = return_array()
print('returned_array', returned_array, sep='\n')

array = np.arange(3, dtype=float)
print('array', array, sep='\n')
square_array(array)
print('squared array', array, sep='\n')

print('sum squared array', sum_array(array))
