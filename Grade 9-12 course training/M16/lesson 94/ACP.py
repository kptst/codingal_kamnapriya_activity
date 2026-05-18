#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import dataset
data = sns.load_dataset('iris')

#find median value of Feature species
categories = ['setosa','virginica','versicolor']
data['flower_num'] = pd.Categorical(data['species'], categories, ordered=True)
median_value = np.median(data['flower_num'].cat.codes)
median_text = categories[int(median_value)]
print("Median Value of Species -", median_text)
#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import dataset
data = sns.load_dataset('iris')

#find the frequency of each category
print("Frequency of each category of Species feature")
print(data['species'].value_counts())
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import dataset
data = pd.read_csv('Churn.csv')

# create bar chart
sns.countplot(data['region_category'], order=data['region_category'].value_counts().index, palette='winter')