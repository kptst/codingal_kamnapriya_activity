sns.heatmap(df_weather.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()