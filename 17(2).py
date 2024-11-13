import pandas as pd
import numpy as np


name = 'table.txt'

lst = []

data = np.loadtxt(name, dtype=int)
for i in range(len(data)):
    for j in range(len(data)):
        if i == j:
            lst.append(data[i][j])
        if j == len(data) - i - 1:
            lst.append(data[i][j])

ar = np.array(lst)
df = pd.Series(ar)

df.to_csv("diag.txt")
print(df)