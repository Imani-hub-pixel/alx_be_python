import mysql.connector
print("mysql.connector imported successfully!")
mydb=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Faith@2025",
    database="StudentInfo"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM student ORDER BY StudentId ASC")
rows=mycursor.fetchall()
for row in rows:
    print(row)
mycursor.close()
mydb.close()

