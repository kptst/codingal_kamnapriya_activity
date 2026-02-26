SELECT name, marks
FROM students
WHERE marks = (SELECT MAX(marks) FROM students);


--#Python version

import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
SELECT name, marks
FROM students
WHERE marks > (SELECT AVG(marks) FROM students)
""")

for row in cursor.fetchall():
    print(row)

conn.close()