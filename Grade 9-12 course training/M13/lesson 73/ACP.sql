import sqlite3

# 1️⃣ Connect to SQLite Database (creates file if not exists)
conn = sqlite3.connect("mydatabase.db")

# 2️⃣ Create Cursor
cursor = conn.cursor()

# 3️⃣ Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    marks INTEGER
)
""")

# 4️⃣ Insert Data
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Aman", 15))
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Riya", 7))
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Karan", 18))

# 5️⃣ Commit Changes
conn.commit()

# 6️⃣ Fetch Data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# 7️⃣ Close Connection
conn.close()