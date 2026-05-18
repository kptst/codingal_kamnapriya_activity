####**Import Libraries**
# dataset-https://drive.google.com/file/d/130chrCClkdqpJAx-6uFTkgZOl9b7geg5/view?usp=sharing
# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

"""####**Check Null Values**"""

data.isnull().sum()

"""**Null values present in Cabin -**

#### **Boxplot of Feature Age and Pclass**
"""

plt.boxplot(data['Age'])
plt.title('Age distribution')
plt.show()

plt.boxplot(data['Pclass'])
plt.title('Passenger Class distribution')
plt.show()