import sqlite3

conn = sqlite3.connect('demo.sqlite3')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS department(
        dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
        dept_name TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    emp_name TEXT NOT NULL,
    salary INTEGER NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES department (dept_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    )
""")

# cursor.executemany("""
#     INSERT INTO department (dept_name) VALUES(?)
# """,[
#     ('HR',),
#     ('Engineering',),
#     ('Sales',)
# ])

conn.commit()

cursor.executemany("""
    INSERT INTO employee (emp_name,salary,dept_id) VALUES(?,?,?)
""",[
    ('Albin',50000,1),
    ('Abhiram',60000,1),
    ('krish',80000,2),
    ('Hari',25000,2),
    ('john',75000,3),
    ('peter',90000,3)
])

# cursor.execute("""
#     SELECT e.emp_id,e.emp_name, e.salary
#     FROM employee e JOIN department d ON e.dept_id = d.dept_id
# """)
# data = cursor.fetchall()
# print(data)

# cursor.execute("""
#     SELECT e.emp_id,e.emp_name, e.salary
#     FROM employee e JOIN department d ON e.dept_id = d.dept_id
#     WHERE d.dept_name ='Engineering'
# """)
# data = cursor.fetchall()
# print(data)

cursor.execute("""
    SELECT department, SUM(salary) AS total_salary
    FROM employees
    GROUP BY department
""")
data = cursor.fetchall()
for row in data:
    print(row)

cursor.execute("""
    SELECT department, AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
""")
data = cursor.fetchall()
for row in data:
    print(row)

cursor.execute("""
    SELECT department, SUM(salary) AS total_salary
    FROM employees
    GROUP BY department
    HAVING SUM(salary) > 100000
""")
data = cursor.fetchall()
for row in data:
    print(row)

# cursor.execute("""
#     UPDATE employees
#     SET department = 'Engineering'
#     WHERE employee_id = 1
# """)
# conn.commit()
# print("Employee moved successfully.")

cursor.execute("""
    UPDATE employees
    SET salary = salary * 1.10
    WHERE department = 'HR'
""")
conn.commit()
print("Salary updated successfully.")

# cursor.execute("""
#     DELETE FROM department
#     WHERE department_name = 'Sales'
# """)
# conn.commit()
# print("Sales department deleted successfully.")

cursor.execute("""
    SELECT *
    FROM employees
""")
data = cursor.fetchall()
for row in data:
    print(row)

cursor.execute("""
    SELECT *
    FROM employees
    WHERE dept_id NOT IN (
        SELECT dept_id FROM department
    )
""")
data = cursor.fetchall()
print(data)
