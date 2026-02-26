import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

weather = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Temperature": [30, 32, 35, 31, 29],
    "Humidity": [60, 65, 55, 70, 75]
}

df_weather = pd.DataFrame(weather)

sns.lineplot(x="Day", y="Temperature", data=df_weather)
plt.title("Temperature Trend")
plt.show()