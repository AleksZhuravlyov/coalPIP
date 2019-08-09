import sys
import os
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

from cpp2p_demo.some import SomeWrapper


some_A = SomeWrapper(var_bool=bool(True),
                     var_int=int(42),
                     var_float=float(3.14),
                     var_str=str('yep'),
                     var_array_bool=np.array([True, False, True], dtype=bool),
                     var_array_int=np.array([0, 1, 2], dtype=np.int32),
                     var_array_float=np.array([0.1, 1.1, 2.1], dtype=float),
                     var_array_str=np.array(['zero', 'one', 'two'], dtype=str))

print()
print('var_bool_A', some_A.var_bool)
print('var_int_A ', some_A.var_int)
print('var_float_A ', some_A.var_float)
print('var_str_A ', some_A.var_str)
print('var_array_bool_A ', some_A.var_array_bool)
print('var_array_int_A ', some_A.var_array_int)
print('var_array_float_A ', some_A.var_array_float)
print('var_array_str_A ', some_A.var_array_str)


some_B = SomeWrapper()

print()
print('var_bool_B', some_B.var_bool)
print('var_int_B ', some_B.var_int)
print('var_float_B ', some_B.var_float)
print('var_str_B ', some_B.var_str)
print('var_array_bool_B ', some_B.var_array_bool)
print('var_array_int_B ', some_B.var_array_int)
print('var_array_float_B ', some_B.var_array_float)
print('var_array_str_B ', some_B.var_array_str)


some_B.var_bool = bool(False)
some_B.var_int = int(84)
some_B.var_float = float(6.28)
some_B.var_str = str('nope')
some_B.var_array_bool = np.array([True, False, True], dtype=bool)
some_B.var_array_int = np.array([0, 1, 2], dtype=np.int32)
some_B.var_array_float = np.array([0.1, 1.1, 2.1], dtype=float)
some_B.var_array_str = np.array(['zero', 'one', 'two'], dtype=str)

print()
print('var_bool_B', some_B.var_bool)
print('var_int_B ', some_B.var_int)
print('var_float_B ', some_B.var_float)
print('var_str_B ', some_B.var_str)
print('var_array_bool_B ', some_B.var_array_bool)
print('var_array_int_B ', some_B.var_array_int)
print('var_array_float_B ', some_B.var_array_float)
print('var_array_str_B ', some_B.var_array_str)
print()


some = SomeWrapper()

some.say_hi()
print(some.return_hi())
some.say_word("test")
print(some.return_word("test"))
