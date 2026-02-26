import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Area": [500, 700, 900, 1100, 1300],
    "Rent": [8000, 12000, 15000, 20000, 25000]
}

df = pd.DataFrame(data)

sns.regplot(x="Area", y="Rent", data=df)
plt.title("Housing Rent Prediction")
plt.show()