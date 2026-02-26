import sqlite3

# Connect to database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# 1️⃣ Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER
)
""")
print("Table Created Successfully")

# 2️⃣ Insert Data
students_data = [
    ("Aman", 15),
    ("Riya", 7),
    ("Karan", 18),
    ("Simran", 10)
]

cursor.executemany("INSERT INTO students (name, marks) VALUES (?, ?)", students_data)
conn.commit()
print("Data Inserted Successfully")

# 3️⃣ View Table Data
print("\nAll Student Records:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# 4️⃣ Update Data
cursor.execute("UPDATE students SET marks = 12 WHERE name = 'Riya'")
conn.commit()
print("\nRecord Updated Successfully")

# 5️⃣ Delete Data
cursor.execute("DELETE FROM students WHERE name = 'Simran'")
conn.commit()
print("Record Deleted Successfully")

# 6️⃣ Show Updated Table
print("\nUpdated Student Records:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# 7️⃣ Drop Table (Uncomment if needed)
# cursor.execute("DROP TABLE students")
# print("Table Dropped Successfully")

# Close Connection
conn.close()