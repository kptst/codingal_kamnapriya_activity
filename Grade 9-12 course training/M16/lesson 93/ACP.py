#import libraries
import pandas as pd
import numpy as np
import seaborn as sns

#import dataset
data = sns.load_dataset('iris')

# calculate quartiles
data_q1 = np.quantile(data['petal_length'], 0.25)
data_q2 = np.quantile(data['petal_length'], 0.50)
data_q3 = np.quantile(data['petal_length'], 0.75)

print("First Quartile (Q1) -", data_q1)
print("Second Quartile (Q2) -", data_q2)
print("Third Quartile (Q3) -", data_q3)
# import libraries
import pandas as pd
import numpy as np
import seaborn as sns

# import dataset
data = sns.load_dataset('iris')

# calculate quartiles
data_ten_percent = np.quantile(data['petal_length'], 0.10)
data_thirty_three_percent = np.quantile(data['petal_length'], 0.33)

print("The value that splits 10% of the data is   -", data_ten_percent)
print("The value that splits 33% of the data is   -", data_thirty_three_percent)
# import libraries
import pandas as pd
import numpy as np
import seaborn as sns

# import dataset
data = sns.load_dataset('iris')

# calculate quartiles
Q1 = np.quantile(data['petal_length'], 0.25)
Q3 = np.quantile(data['petal_length'], 0.75)

IQR = Q3-Q1
print("Inter-Quartile Range is ", IQR)