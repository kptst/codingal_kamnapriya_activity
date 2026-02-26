-- Create Table
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER,
    department TEXT
);

-- Insert Data
INSERT INTO students (name, marks, department) VALUES
('Aman', 15, 'CSE'),
('Riya', 7, 'IT'),
('Karan', 18, 'CSE'),
('Simran', 10, 'ECE');

-- Display All Records
SELECT * FROM students;

-- Display Name and Marks Only
SELECT name, marks FROM students;

-- Students with marks > 10
SELECT * FROM students WHERE marks > 10;

-- Students between 8 and 15
SELECT * FROM students WHERE marks BETWEEN 8 AND 15;

-- Sort Ascending
SELECT * FROM students ORDER BY marks ASC;

-- Sort Descending
SELECT * FROM students ORDER BY marks DESC;

-- Count Students
SELECT COUNT(*) FROM students;

-- Highest Marks
SELECT MAX(marks) FROM students;

-- Lowest Marks
SELECT MIN(marks) FROM students;

-- Average Marks
SELECT AVG(marks) FROM students;

-- Group by Department
SELECT department, COUNT(*) FROM students GROUP BY department;

-- Update Marks
UPDATE students SET marks = 20 WHERE name = 'Aman';

-- Delete Record
DELETE FROM students WHERE name = 'Riya';

-- Add Column
ALTER TABLE students ADD COLUMN age INTEGER;

-- Rename Table
ALTER TABLE students RENAME TO student_info;