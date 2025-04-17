import numpy as np
import pandas as pd

x = np.random.randint(1, 30, 10)
print(x)

grocery_list = np.array(['milk', 'rice', 'eggs', 'bread', 'oranges', 'water'])
print(grocery_list[-1])

df = pd.DataFrame({'person_id': [0, 1, 2, 3],
                   'age': [21, 25, 62, 43],
                   'height': [1.61, 1.87, 1.49, 2.01]}
                  ).set_index('person_id')

print(df["age"].std())
print(df.columns)