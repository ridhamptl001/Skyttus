CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);

INSERT INTO students (student_id, name, department, year, marks)
VALUES
(1, 'Ridham', 'CSE', 3, 85),
(2, 'Rohil', 'IT', 3, 72),
(3, 'Amit', 'CSE', 2, 91),
(4, 'Neha', 'ECE', 4, 68),
(5, 'Rohan', 'IT', 3, 78),


-- 1. Display all student records
SELECT *
FROM students;


-- 2. Display only name and department
SELECT name, department
FROM students;


-- 3. Find students with marks greater than 75
SELECT *
FROM students
WHERE marks > 75;


-- 4. Display students from CSE department
SELECT *
FROM students
WHERE department = 'CSE';


-- 5. Sort students by marks in descending order
SELECT *
FROM students
ORDER BY marks DESC;


-- 6. Display top 3 scorers
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 3;