import pyodbc

server = 'localhost'
database = 'MasterDB'
string_conexao = 'Driver={SQL Server Native CLient 11.0};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
c = pyodbc.connect(string_conexao)
cur=c.cursor()

def checklogin(login,password):
    cur.execute(f'''
        select * from Login where Login=('{login}') and Password=('{password}') and (situacao=1)
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
    select * from login where Login=('{acconunt}') and Password=('{passowrd}') and situacao=1
    ''')
    valida=cur.fetchall()
    if len(valida)==0:
        cur.execute(f'''
        insert into login (Login,Password,situacao) values('{acconunt}','{passowrd}',1)
        ''')
        cur.commit()
        return ('Conta Criada com sucesso')
    elif valida !=0:
        return ('Conta ja em uso')

