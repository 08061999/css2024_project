# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:46:57 2024

@author: user
"""

import pandas as pd

df = pd.read_csv("C:/Users/user/Desktop/css2024_project/css2024_project/movie_dataset.csv")

print(df)


x = df["Revenue (Millions)"].mean()

df["Revenue (Millions)"].fillna(x, inplace = True) 


x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace = True) 

print(df.describe())


