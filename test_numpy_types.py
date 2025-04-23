import numpy as np


my_array = np.array([124] * 1000000)

print(my_array.nbytes)

my_array = np.array([124] * 1000000, dtype='i1')

print(my_array.nbytes)


x = np.zeros((3, 5, 2), dtype=np.complex128)
