SELECT students.name, departments.dept_name
FROM students
LEFT JOIN departments
ON students.dept_id = departments.dept_id;

--Python Version
import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
SELECT students.name, departments.dept_name
FROM students
INNER JOIN departments
ON students.dept_id = departments.dept_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()