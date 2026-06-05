import sqlite3

conn = sqlite3.connect('employee.sqlite3')

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

cursor.executemany("""
    INSERT INTO department (dept_name) VALUES(?)
""",[
    ('HR',),
    ('Software',),
    ('Marketing',)
])
conn.commit()
cursor.executemany("""
    INSERT INTO employee (emp_name,salary,dept_id) VALUES(?,?,?)
""",[
    ('Nigin',50000,1),
    ('Abhiram',60000,2),
    ('Abhin',80000,2),
    ('Hari',25000,3),
    ('Krishna',75000,3),
])
conn.commit()
# cursor.execute("""
#     DELETE
#     FROM employee
#     WHERE emp_id = 6
# """)
# conn.commit()

cursor.execute("""
    SELECT e.emp_id,e.emp_name, e.salary
    FROM employee e JOIN department d ON e.dept_id = d.dept_id
    WHERE d.dept_name ='Software'
""")
data = cursor.fetchall()
print(data)

conn.close()