import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    # databas'novavi'
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS novavi")
cursor.execute("USE novavi")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20),
        age INT
    )
""")

# cursor.execute("INSERT INTO students(name,age) VALUES (%s,%s)",('Akhil', 20))

# cursor.execute("INSERT INTO students(name,age) VALUES (%s,%s)",('Goutham', 22))

# conn.commit()

cursor.execute("""
    SELECT *
    FROM students
""")

# cursor.execute("""
#     SELECT name
#     FROM students
#     WHERE age >= 18
# """)

# cursor.execute("""
#     UPDATE students
#     SET name=%s
#     WHERE id=%s
# """, ('Goutham', 3))

# cursor.execute("""
#     UPDATE students
#     SET name=%s
#     WHERE id=%s
# """, ('Akhil', 4))
# conn.commit()

# cursor.execute("""
#     SELECT name, age
#     FROM students
#     WHERE age>=%s
# """,(18,))

print(cursor.fetchall())