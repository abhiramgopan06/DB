import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS library")
cursor.execute("USE library")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(100),
        genre VARCHAR(50),
        price DECIMAL(10,2),
        published_year INT,
        rating FLOAT
    )
""")

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search By Author")
    print("4. Search By Genre")
    print("5. Books Price Greater Than")
    print("6. Top Rated Books")
    print("7. Books Published After Year")
    print("8. Search Title")
    print("9. Count Books By Genre")
    print("10. Average Price By Genre")
    print("11. Genre And Rating Filter")
    print("12. Update Book Price")
    print("13. Update Book Rating")
    print("14. Delete Book By ID")
    print("15. Delete Books By Genre")
    print("16. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")
        price = float(input("Enter Price: "))
        year = int(input("Enter Published Year: "))
        rating = float(input("Enter Rating: "))

        cursor.execute("""
            INSERT INTO books(title,author,genre,price,published_year,rating)
            VALUES(%s,%s,%s,%s,%s,%s)
        """, (title, author, genre, price, year, rating))

        conn.commit()
        print("Book Added Successfully")

    elif choice == 2:
        cursor.execute("""
            SELECT *
            FROM books
        """)

        print(cursor.fetchall())

    elif choice == 3:
        author = input("Enter Author: ")

        cursor.execute("""
            SELECT *
            FROM books
            WHERE author=%s
        """, (author,))

        print(cursor.fetchall())

    elif choice == 4:
        genre = input("Enter Genre: ")

        cursor.execute("""
            SELECT *
            FROM books
            WHERE genre=%s
        """, (genre,))

        print(cursor.fetchall())

    elif choice == 5:
        price = float(input("Enter Minimum Price: "))

        cursor.execute("""
            SELECT *
            FROM books
            WHERE price>%s
        """, (price,))

        print(cursor.fetchall())

    elif choice == 6:
        cursor.execute("""
            SELECT *
            FROM books
            ORDER BY rating DESC
            LIMIT 5
        """)

        print(cursor.fetchall())

    elif choice == 7:
        year = int(input("Enter Year: "))

        cursor.execute("""
            SELECT *
            FROM books
            WHERE published_year>%s
        """, (year,))

        print(cursor.fetchall())

    elif choice == 8:
        title = input("Enter Title Keyword: ")

        cursor.execute("""
            SELECT *
            FROM books
            WHERE title LIKE %s
        """, ('%' + title + '%',))

        print(cursor.fetchall())

    elif choice == 9:
        cursor.execute("""
            SELECT genre, COUNT(*) AS total
            FROM books
            GROUP BY genre
        """)

        print(cursor.fetchall())

    elif choice == 10:
        cursor.execute("""
            SELECT genre, AVG(price) AS average_price
            FROM books
            GROUP BY genre
        """)

        print(cursor.fetchall())

    elif choice == 11:
        genre = input("Enter Genre: ")
        rating = float(input("Enter Minimum Rating: "))

        cursor.execute("""
            SELECT *
            FROM books
            WHERE genre=%s AND rating>%s
        """, (genre, rating))

        print(cursor.fetchall())

    elif choice == 12:
        book_id = int(input("Enter Book ID: "))
        price = float(input("Enter New Price: "))

        cursor.execute("""
            UPDATE books
            SET price=%s
            WHERE book_id=%s
        """, (price, book_id))

        conn.commit()
        print("Price Updated")

    elif choice == 13:
        book_id = int(input("Enter Book ID: "))
        rating = float(input("Enter New Rating: "))

        cursor.execute("""
            UPDATE books
            SET rating=%s
            WHERE book_id=%s
        """, (rating, book_id))

        conn.commit()
        print("Rating Updated")

    elif choice == 14:
        book_id = int(input("Enter Book ID: "))

        cursor.execute("""
            DELETE FROM books
            WHERE book_id=%s
        """, (book_id,))

        conn.commit()
        print("Book Deleted")

    elif choice == 15:
        genre = input("Enter Genre: ")

        cursor.execute("""
            DELETE FROM books
            WHERE genre=%s
        """, (genre,))

        conn.commit()
        print("Genre Books Deleted")

    elif choice == 16:
        print("Program Closed")
        break

    else:
        print("Invalid Choice")

conn.close()