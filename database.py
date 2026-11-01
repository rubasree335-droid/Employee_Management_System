import mysql.connector


def init_db():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS project")
    cur.execute("USE project")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            dept_id INT AUTO_INCREMENT PRIMARY KEY,
            dept_name VARCHAR(100) NOT NULL,
            manager VARCHAR(100),
            location VARCHAR(100)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            gender VARCHAR(10),
            dob DATE,
            contact VARCHAR(15),
            salary INT,
            dept_id INT,
            FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
                ON DELETE SET NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            att_id INT AUTO_INCREMENT PRIMARY KEY,
            emp_id INT NOT NULL,
            att_date DATE NOT NULL,
            status ENUM('Present','Absent','Leave') NOT NULL,
            UNIQUE KEY unique_attendance(emp_id, att_date),
            FOREIGN KEY (emp_id) REFERENCES employees(id)
                ON DELETE CASCADE
        )
    """)

    con.commit()
    cur.close()
    con.close()


def connect_db():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SQL123",
        database="project"
    )
    return con



init_db()