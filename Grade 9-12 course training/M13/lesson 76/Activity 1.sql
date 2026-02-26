CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    marks INTEGER CHECK (marks >= 0 AND marks <= 20),
    department TEXT DEFAULT 'CSE'
);
--#Python Version
import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    marks INTEGER CHECK (marks >= 0 AND marks <= 20),
    department TEXT DEFAULT 'CSE'
)
""")

cursor.execute("PRAGMA table_info(students)")
print(cursor.fetchall())

conn.close()