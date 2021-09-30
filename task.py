import pandas as pd
import seaborn as sb
import numpy as np
import os

df=pd.read_csv('Placement_Data_Full_Class.csv')

print(df.isnull().sum())
df=df.fillna(0)
print(df)

df=df.drop(columns="ssc_b")
df=df.drop(columns="hsc_b")
print(df.columns)
print(df)
