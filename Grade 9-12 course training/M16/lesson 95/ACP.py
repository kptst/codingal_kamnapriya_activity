# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import dataset
data = pd.read_csv('train (1).csv')

# find bin range
min = data['age'].min()
max = data['age'].max()
print("Minimum -", min)
print("Maximum -", max)

Minimum - 10
Maximum - 64

# Store the boundaries
bins = [10, 20, 30, 40, 50, 60, 70]

# Create new binned_age column that bins the values of the 'Age' column
data['binned_age'] = pd.cut(data['age'], bins)

# Print the first few rows of the data
print(data[['binned_age', 'age']].head())

# Store the labels for our bins
age_labels = ['Young', 'Young Adult', 'Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']

# Bin the values of the 'Age' column and specify the labels
data['binned_age'] = pd.cut(data['age'], bins, labels = age_labels)

print(data[['binned_age', 'age']].head())

import pandas as pd

# read in data
election_data = pd.read_csv('election_data.csv')

# get the counts for each candidate
votes = election_data['vote'].value_counts()
print(votes)

mask = election_data.isin(votes[votes < 200].index)

election_data[mask] = 'other'
print(election_data['Vote'].value_counts())

# check skewness of feature days_since_last_login
sns.distplot(data['days_since_last_login'])
plt.show()
print('Skewness -', data['days_since_last_login'].skew())
from sklearn.preprocessing import PowerTransformer

# log transform
log_transform = PowerTransformer()
log_transform.fit_transform(data)

sns.boxplot(data = data, x = 'region_category', y = 'avg_transaction_value')
plt.show()
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import dataset
data = pd.read_csv('Churn Data.csv')

# Check correlation between membership category and gender
association_categorical = pd.crosstab(data['membership_category'], data['gender'])
print(association_categorical)
# Check association between Age and avg_time_spent
plt.scatter(y = data['churn_risk_score'], x = data['avg_transaction_value'])
plt.xlabel('Churn Risk Score')
plt.ylabel('Average Transaction Value')
plt.show()