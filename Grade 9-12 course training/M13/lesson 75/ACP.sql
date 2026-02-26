import sqlite3

# Connect to Database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER,
    department TEXT
)
""")

# Insert Data
cursor.executemany("""
INSERT INTO students (name, marks, department)
VALUES (?, ?, ?)
""", [
    ("Aman", 15, "CSE"),
    ("Riya", 7, "IT"),
    ("Karan", 18, "CSE"),
    ("Simran", 10, "ECE")
])

conn.commit()

# Execute Queries
print("All Records:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\nStudents with marks > 10:")
for row in cursor.execute("SELECT * FROM students WHERE marks > 10"):
    print(row)

print("\nSorted by Marks (Descending):")
for row in cursor.execute("SELECT * FROM students ORDER BY marks DESC"):
    print(row)

print("\nTotal Students:")
print(cursor.execute("SELECT COUNT(*) FROM students").fetchone()[0])

print("\nHighest Marks:")
print(cursor.execute("SELECT MAX(marks) FROM students").fetchone()[0])

print("\nAverage Marks:")
print(cursor.execute("SELECT AVG(marks) FROM students").fetchone()[0])

# Update Record
cursor.execute("UPDATE students SET marks = 20 WHERE name = 'Aman'")
conn.commit()

# Delete Record
cursor.execute("DELETE FROM students WHERE name = 'Riya'")
conn.commit()

print("\nFinal Records:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

# Close Connection
conn.close()