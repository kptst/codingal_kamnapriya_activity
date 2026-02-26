CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER
);

CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
);
SELECT students.name, departments.dept_name
FROM students
INNER JOIN departments
ON students.dept_id = departments.dept_id;