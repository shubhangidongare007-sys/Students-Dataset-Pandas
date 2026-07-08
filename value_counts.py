import pandas as pd

df = pd.read_csv("student.csv")
print(df["Course"].value_counts())