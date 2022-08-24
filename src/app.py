#1 Imports
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns

#2 Load & read
df = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv')

#3 Convert the variables
for var in ["neighbourhood", "neighbourhood_group", "room_type", "host_id"]:
  df[var] = pd.Categorical(df[var])

df["last_review"] = df["last_review"].astype("datetime64")

#4 Drop columns
droper = ['id','host_name']
df = df.drop(droper, axis=1)


#5 Dropping data with price=0
df = df[df['price']!=0]

#6 Deal with missing values
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

#7 Encoding categorical variables
df['room_type'] = df['room_type'].map({'Entire home/apt' : 0, 'Private room': 1, 'Shared room': 2})
df['neighbourhood_group'] = df['neighbourhood_group'].map({'Bronx' : 0, 'Brooklyn': 1, 'Manhattan': 2, 'Queens': 3, 'Staten Island': 4})

#8 Save the processed dataframe
df.to_csv('/workspace/EDA/data/processed/data_processed.csv')