import mysql.connector
#與mysql連線
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

my_cursor = mydb.cursor()
#建立資料庫
#my_cursor.execute("CREATE DATABASE User")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
