import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('heart.csv')
print(df.head())
df.shape()
df.info()
df.isnull().sum
df.columns
df.hist(figsize=(15,8),bins=30)
sns.barplot(data=df,x='sex',y='fbs', hue='target',palette='coolwarm')
plt.show()
df['chol'].value_counts()
df['age'].value_counts()
sns.countplot(data=df,x='chol',palette='coolwarm',hue='target')
plt.show()
df.plot(kind="box",layout=(7,8),figsize=(12,8),color="r")
plt.show
plt.figure(figsize=(20,10))
sns.barplot(data=df,x='trestbps', y='restecg', hue="target",palette='pastel')
plt.show()
plt.figure(figsize=(15,10))
sns.heatmap(df.corr(), annot=True)
sns.pairplot(df, hue='sex')
plt.show()
sns.countplot(x='sex', data=df, palette='husl', hue='target')
sns.countplot(x='target', data=df, palette='BuGn')
sns.countplot(x='ca', hue="target", data=df)