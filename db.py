from mysql.connector import (connection)
mydb = connection.MySQLConnection(host='127.0.0.1', user='root', password='Senha123@', database='Fist_db')
mycursor=mydb.cursor()

def checklogin(login,passwoard):
    mycursor.execute(f'''
    select * from Login where user=('{login}') and password=('{passwoard}')
    ''')
    result = mycursor.fetchall()
    if len(result)==1:
        result=True

    elif len(result)==0:
        result=False

    return print(result)
