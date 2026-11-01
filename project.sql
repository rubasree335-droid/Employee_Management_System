create database project;
use project;

CREATE TABLE employees(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    dob DATE,
    contact VARCHAR(15)
);
ALTER TABLE employees
ADD salary INT;
select*from employees;

ALTER TABLE employees ADD dept_id INT;

CREATE TABLE departments (
    dept_id   INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    manager   VARCHAR(100),
    location  VARCHAR(100)
);

ALTER TABLE employees
ADD FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
ON DELETE SET NULL;


CREATE TABLE attendance (
    att_id   INT AUTO_INCREMENT PRIMARY KEY,
    emp_id   INT NOT NULL,
    att_date DATE NOT NULL,
    status   ENUM('Present','Absent','Leave') NOT NULL,
    FOREIGN KEY (emp_id) REFERENCES employees(id)
    ON DELETE CASCADE
);


INSERT INTO departments (dept_name, manager, location) VALUES
('Human Resources', 'Alice', 'Block A'),
('Engineering',     'Bob',   'Block B'),
('Finance',         'Carol', 'Block C'),
('Marketing',       'David', 'Block D');