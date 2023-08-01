from frictionless import Package
import pandas as pd

df = pd.read_excel("download/Mega-Sena.xlsx", index_col=0)
df.to_csv("data/Mega-Sena.csv")
