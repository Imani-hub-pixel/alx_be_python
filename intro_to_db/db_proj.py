import mysql.connector  

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Faith@2025",
    database="LibraryManagementSystem"
)
mycursor=mydb.cursor()

title=input("Enter book title: ")
author=input("Enter book author: ")
isbn=input("Enter book ISBN: ")

sql="INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
val=(title, author, isbn)
mycursor.execute(sql, val)
mydb.commit()


#allow users to search for books by title
title_search=input("Enter book title to search: ")
sql="SELECT * FROM books WHERE title=%s"
val=(title_search,)
mycursor.execute(sql, val)
results=mycursor.fetchall()
for row in results:
    print(row)

#Printing the details of all books in the database
mycursor.execute("SELECT * FROM books ORDER BY id ASC")
rows=mycursor.fetchall()
for row in rows:
    print(row)


sql="DELETE FROM books WHERE id=1"
mycursor.execute(sql)
mydb.commit()

mycursor.close()
mydb.close()