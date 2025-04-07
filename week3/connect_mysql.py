import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="u1853252_myisrodi",
  password="@myisrodi.comtr"
)
# "mysql:host=localhost;dbname=u1853252_isrodicomtr;charset=utf8",'u1853252_myisrodi','@myisrodi.comtr')
print(mydb)