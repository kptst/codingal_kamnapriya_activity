import matplotlib.pyplot as plt

students = ["Aman", "Riya", "Karan", "Simran"]
marks = [15, 7, 18, 10]

# Line Graph
plt.plot(students, marks)
plt.title("Marks Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Graph
plt.bar(students, marks)
plt.title("Marks Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()