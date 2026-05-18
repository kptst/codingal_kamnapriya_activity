#Housing Rent Prediction- In this project, you will visualize and predict house rent.
# =========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files

uploaded = files.upload()

# Load Dataset
df = pd.read_csv('USA_Housing (1).csv')
print(df.head())
print(df.columns)
# Income vs Price
plt.figure(figsize=(8,6))

sns.scatterplot(
    x='Avg. Area Income',
    y='Price',
    data=df
)

plt.title('Income vs Price')
plt.xlabel('Average Area Income')
plt.ylabel('House Price')

plt.show()

# Rooms vs Price
plt.figure(figsize=(8,6))

sns.scatterplot(
    x='Avg. Area Number of Rooms',
    y='Price',
    data=df
)

plt.title('Rooms vs Price')
plt.xlabel('Average Area Number of Rooms')
plt.ylabel('House Price')

plt.show()
sns.pairplot(
    df.select_dtypes(include=[np.number])
)

plt.show()

# =========================================
# Correlation Heatmap
# =========================================

plt.figure(figsize=(12,8))

sns.heatmap(
    df.select_dtypes(include=[np.number]).corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')

plt.show()