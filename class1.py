import csv
import os
import math
import pandas as pd
os.system("cls")

df = pd.read_csv("class1.csv")
marks = df["Marks"].tolist()
sum = 0
for i in marks:
    sum+=int(i)
mean = sum/len(marks)
s = 0
for i in marks:
    sub = int(i)-mean
    sq = sub**2
    s+=sq

total = s/(len(marks)-1)
result = math.sqrt(total)
print(result)

