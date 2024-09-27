import sqlite3 

conexao = sqlite3.connect("clientes.sqlite")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
        )
    
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registros(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def excluir_registros(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()


#dados = [
 #   ("Marcos", "marcos@gmail.com"),
  #  ("Valesca", "valesca@gmail.com"),
  #  ("Tesla", "tesla@gmail.com"),
#]

#inserir_muitos(conexao, cursor, dados)

def visualizar_clientes(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

cliente = visualizar_clientes(cursor, 2)
#print(cliente)

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)



