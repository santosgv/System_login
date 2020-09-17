from mysql.connector import (connection)
mydb = connection.MySQLConnection(host='127.0.0.1', user='root', password='Senha123@', database='Fist_db')
mycursor=mydb.cursor()


def checklogin(login,passwoard):
    mycursor.execute(f'''
        select * from Login where user=('{login}') and password=('{passwoard}')
        ''')
    status = mycursor.fetchall()
    if len(status)==1:
        status=True

    elif len(status)==0:
        status=False

    elif len(status) !=(0,1):
        status='Foi encontrado mas de um resultado para o usuario'

    return status
