import time

import pandas as pd
import random

t0 = time.time()
my_list = [random.randint(0, 10000000) for i in range(100000000)]

my_ds = pd.Series(my_list)
print(len(my_list))

t1 = time.time()
my_max1 = max(my_list)
t2 = time.time()
my_max2 = my_ds.max()
t3 = time.time()

print(f"Creation time = {t1-t0}")
print(f"Max for list cost = {t2-t1}")
print(f"Max for ps cost = {t3-t2}")
