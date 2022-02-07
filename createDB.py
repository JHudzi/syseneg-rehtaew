import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    port = "3000",
    user = "root",
    password = "Password123",
)

my_cursor = db.cursor()

my_cursor.execute("CREATE DATABASE weather1")

my_cursor.execute("SHOW DATABASES")
for i in my_cursor:
    print(i)