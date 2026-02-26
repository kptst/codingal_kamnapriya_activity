SELECT name, marks
FROM students
WHERE marks > (SELECT AVG(marks) FROM students);