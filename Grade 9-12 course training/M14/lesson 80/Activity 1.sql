import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Karan", "Simran"],
    "Marks": [15, 7, 18, 10],
    "Department": ["CSE", "IT", "CSE", "ECE"]
}

df = pd.DataFrame(data)

print(df)