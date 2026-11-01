from database import connect_db

def add_employee(name, age, gender, dob, contact,salary):
    try:
        con = connect_db()
        cur = con.cursor()

        query = """INSERT INTO employees
                   (name, age, gender, dob, contact,salary)
                   VALUES (%s,%s,%s,%s,%s,%s)"""

        cur.execute(query, (name, age, gender, dob, contact,salary))
        con.commit()
        con.close()

        print("Employee Added")

    except Exception as e:
        print("Error:", e)


def view_employee():
    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()

    con.close()
    return data
        
        
def delete_employee(emp_id):
    con = connect_db()
    cur = con.cursor()

    cur.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    con.commit()
    con.close()
    
def update_employee(emp_id, name, age, gender, dob, contact,salary):
    con = connect_db()
    cur = con.cursor()

    query = """UPDATE employees
               SET name=%s, age=%s, gender=%s,
                   dob=%s, contact=%s,salary=%s
               WHERE id=%s"""

    cur.execute(query, (name, age, gender, dob, contact,salary, emp_id))
    con.commit()
    con.close()

def clear_all():
    con = connect_db()
    cur = con.cursor()

    cur.execute("DELETE FROM employees")
    con.commit()
    con.close()

def search_employee(emp_id):
    con = connect_db()
    cursor = con.cursor()

    query = "SELECT * FROM employees WHERE id=%s"
    cursor.execute(query,(emp_id,))

    result = cursor.fetchone()

    con.close()
    return result


def employee_count():
    con = connect_db()
    cursor = con.cursor()

    query = "SELECT COUNT(*) FROM employees"
    cursor.execute(query)

    count = cursor.fetchone()[0]

    con.close()
    return count   


def mark_attendance(emp_id, att_date, status):
    try:
        con = connect_db()
        cur = con.cursor()
        query = """INSERT INTO attendance (emp_id, att_date, status)
                   VALUES (%s, %s, %s)
                   ON DUPLICATE KEY UPDATE status = VALUES(status)"""
        cur.execute(query, (emp_id, att_date, status))
        con.commit()
        con.close()
        print("Attendance marked")
    except Exception as e:
        print("Error:", e)


def view_attendance(emp_id=None):
    con = connect_db()
    cur = con.cursor()
    if emp_id:
        cur.execute("""
            SELECT a.att_id, e.name, a.att_date, a.status
            FROM attendance a
            JOIN employees e ON a.emp_id = e.id
            WHERE a.emp_id = %s
            ORDER BY a.att_date DESC
        """, (emp_id,))
    else:
        cur.execute("""
            SELECT a.att_id, e.name, a.att_date, a.status
            FROM attendance a
            JOIN employees e ON a.emp_id = e.id
            ORDER BY a.att_date DESC
        """)
    data = cur.fetchall()
    con.close()
    return data


def attendance_summary(emp_id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
        SELECT status, COUNT(*) FROM attendance
        WHERE emp_id = %s GROUP BY status
    """, (emp_id,))
    rows = cur.fetchall()
    con.close()
    summary = {"Present": 0, "Absent": 0, "Leave": 0}
    for status, cnt in rows:
        summary[status] = cnt
    return summary


def delete_attendance(att_id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM attendance WHERE att_id=%s", (att_id,))
    con.commit()
    con.close()



def add_department(dept_name, manager, location):
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("""INSERT INTO departments (dept_name, manager, location)
                       VALUES (%s, %s, %s)""", (dept_name, manager, location))
        con.commit()
        con.close()
        print("Department Added")
    except Exception as e:
        print("Error:", e)


def view_departments():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM departments")
    data = cur.fetchall()
    con.close()
    return data


def update_department(dept_id, dept_name, manager, location):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""UPDATE departments
                   SET dept_name=%s, manager=%s, location=%s
                   WHERE dept_id=%s""", (dept_name, manager, location, dept_id))
    con.commit()
    con.close()


def delete_department(dept_id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM departments WHERE dept_id=%s", (dept_id,))
    con.commit()
    con.close()


def get_department_names():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT dept_id, dept_name FROM departments")
    data = cur.fetchall()
    con.close()
    return data


def employees_in_department(dept_id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("""SELECT id, name, age, gender, contact, salary
                   FROM employees WHERE dept_id = %s""", (dept_id,))
    data = cur.fetchall()
    con.close()
    return data