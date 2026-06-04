import sqlite3
# connection object
conn = sqlite3.connect('demo.sqlite3')
# cursor object
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER,
#         course TEXT NOT NULL
#     )""")
# name = "Aswin"
# age = 18
# course = 'BCOM'
# cursor.execute("""
#       INSERT INTO students
#       (name,age,course)
#       VALUES ('Akhil',19,'BCA')           
# """)
# cursor.execute("""
#       INSERT INTO students
#       (name,age,course)
#       VALUES (?,?,?)           
# """,(name,age,course))
# conn.commit()
# cursor.execute("""
#       SELECT *5
#       FROM students
# """)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")
conn.commit()
while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        cursor.execute("""
            INSERT INTO students
            (name,age,course)
            VALUES (?,?,?)           
        """,(name,age,course))
        conn.commit()
    elif choice == 2:
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        print("+----+----------+-----+--------+")
        print("| ID | NAME     | AGE | COURSE |")
        print("+----+----------+-----+--------+")
        for row in data:
            print(f"| {row[0]:<2} | {row[1]:<8} | {row[2]:<3} | {row[3]:<6} |")
        print("+----+----------+-----+--------+")
    elif choice == 3:
        id = int(input("Enter ID: "))
        course = input("New Course: ")
        cursor.execute("""
            UPDATE students
            SET course = ?
            WHERE id = ?
        """,(course, id))
        conn.commit()
    elif choice == 4:
        id = int(input("Enter ID: "))
        cursor.execute("""
            DELETE
            FROM students
            WHERE id = ? 
        """,(id,))
        conn.commit()
    elif choice == 5:
        break
conn.close()




# cursor.executemany("""
#     INSERT INTO Students
#     (name,age,course)
#     VALUES (?,?,?) 
# """,[
#     ('Hari',20,'BSC'),
#     ('Krishna',17,'BCOM'),
#     ('Nikhil',21,'BCA'),
#     ('Pavan',20,'BTECH'),
#     ('Vinayak',19,'BTECH'),
# ])
# conn.commit()
# name = 'Akhil'
# course = 'BCA'
# age = 17
# cursor.execute("""
#       SELECT name,age
#       FROM students
#       WHERE age>=? AND course=?
#       ORDER BY age DESC
# """,(age,course))
# data = cursor.fetchall()
# print(data)
# conn.close()

# cursor.execute("""
#     UPDATE students
#     SET age = ?
#     WHERE name = ?
# """,(18,'Nikhil'))

# cursor.execute("""
#     DELETE
#     FROM students
#     WHERE id = ? 
# """,(5,))
# conn.commit()
# cursor.execute("""
#     SELECT COUNT(*) as total
#     FROM students
# """)
# cursor.execute("""
#     SELECT AVG(age) as average
#     FROM students
# """)
# cursor.execute("""
#     SELECT MIN(age)
#     FROM students
# """)
# cursor.execute("""
#     SELECT MAX(age)
#     FROM students
# """)
# cursor.execute("""
#     SELECT SUM(age)
#     FROM students
# """)
# data = cursor.fetchall()
# print(data)
# conn.close()

# cursor.execute("ALTER TABLE students ADD COLUMN email TEXT")
# cursor.execute("ALTER TABLE students RENAME COLUMN course TO department")
# cursor.execute("ALTER TABLE students RENAME TO synnfo")
# cursor.execute('DROP TABLE IF EXIST students')
# conn.commit()