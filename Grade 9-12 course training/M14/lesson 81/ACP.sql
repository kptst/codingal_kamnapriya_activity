average = sum(marks) / len(marks)

plt.bar(students, marks)
plt.axhline(average)
plt.title("Marks with Average Line")
plt.show()