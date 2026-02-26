import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Aman", "Riya", "Karan", "Simran", "Arjun"],
    "Marks": [15, 7, 18, 10, 12],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"]
}

df = pd.DataFrame(data)

# Basic Analysis
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())

# Visualization
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Student Performance")
plt.show()