### Check list para auxiliar nas compras mensais ###

import sqlite3
## Criando banco e cursor ##
con= sqlite3.connect("Lista.db")
cursor= con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Lista (
Cod INTEGER PRIMARY KEY AUTOINCREMENT,
Nome text not null,
Categoria text not null,
Situacao Boolean
);
''')

## Classes ##
class Cadastro():
    def __init__(self,Nome,Categoria):
        self.nome=str(Nome)
        self.categoria=str(Categoria)
    def Cadastrar(self):
        cursor.execute(f'''
        insert into Lista (Nome,Categoria,Situacao) values ('{self.nome}','{self.categoria}',1)''')
        con.commit()
    def Remover(self):
        cursor.execute(f'''
        UPDATE Lista
        Set Situacao=0
        where  (select Cod from Lista where ('{self.nome}''{self.categoria}'))
        ''')
        con.commit()

a=Cadastro('Pera','Fruta')
a.Remover()