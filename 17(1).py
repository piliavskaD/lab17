import pandas as pd
import csv
import math as m


name_f = "data.csv"

df = pd.read_csv(name_f)
print(df)

Q_x = float(input("x: "))
Q_y = float(input("y: "))


lst = []
for i in range(len(df["x"])):
    lst.append(int(Q_x - df["x"][i]))

df["x"] = lst

lst = []
for i in range(len(df["y"])):
    lst.append(int(Q_y - df["y"][i]))


df["y"] = lst
print(df)

lst1 = []

for ind, row in df.iterrows():
    lst1.append(format(m.sqrt(row["x"]**2 + row["y"]**2), ".3f"))
print(lst1)

with open("len.csv", "w") as csvfile:
    w = csv.writer(csvfile)
    w.writerow(["A"] + ["B"] + ["C"] + ["D"])
    w.writerow(lst1)
