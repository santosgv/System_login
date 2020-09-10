from mysql.connector import (connection)
mydb = connection.MySQLConnection(host='127.0.0.1', user='root', password='Senha123@', database='Fist_db')
mycursor=mydb.cursor()