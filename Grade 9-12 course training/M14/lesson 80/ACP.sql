# Display students with marks > 10
print(df[df["Marks"] > 10])

# Add new column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 8 else "Fail")

print(df)

# Sort by Marks
print(df.sort_values(by="Marks"))