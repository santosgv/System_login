import pyodbc

server = 'localhost'
database = 'MasterDB'
string_conexao = 'Driver={SQL Server Native CLient 11.0};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
c = pyodbc.connect(string_conexao)
cur=c.cursor()

def checklogin(login,password):
    cur.execute(f'''
        select * from Login where Login=('{login}') and Password=('{password}')
        ''')
    status = cur.fetchall()
    if len(status)==1:
        status=True

    elif len(status)==0:
        status=False

    elif len(status) !=(0,1):
        status='Foi encontrado mas de um resultado para o usuario'

    return status

def creatlogin(acconunt,passowrd):
    cur.execute(f'''
    select * from Login where Login=('{acconunt}') and Password=('{passowrd}')
    ''')
    valida=cur.fetchall()
    if len(valida)==0:
        cur.execute(f'''
        insert into Login (Login,Password) values('{acconunt}','{passowrd}')
        ''')
        cur.commit()
        return ('Conta Criada com sucesso')
    elif valida !=0:
        return ('Conta ja em uso')