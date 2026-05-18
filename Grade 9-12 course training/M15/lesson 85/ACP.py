# Import Necessary Libraries and Data
from google.colab import files
uploaded = files.upload()
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('penguins_lter.csv')
data.head()
# Check presence of Null Values
data.isnull().any()
data.isnull().sum()
sns.heatmap(data.isnull())

# Handling Numerical Null Values
data['Culmen Depth (mm)'] = data.fillna(data['Culmen Depth (mm)'].mean())
data['Culmen Length (mm)'] = data.fillna(data['Culmen Length (mm)'].mean())
data['Flipper Length (mm)'] = data.fillna(data['Flipper Length (mm)'].mean())
data['Body Mass (g)'] = data.fillna(data['Body Mass (g)'].mean())
data['Delta 13 C (o/oo)'] = data.fillna(data['Delta 13 C (o/oo)'].mean())
data['Delta 15 N (o/oo)'] = data.fillna(data['Delta 15 N (o/oo)'].mean())
# Handling Categorical Null Values
data['Gender'] = data.fillna(data['Gender'].value_counts().index[0])
data = data.drop('Comments', axis=1)
data.isnull().sum()