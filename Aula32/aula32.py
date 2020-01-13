import MySQLdb
conexao  = MySQLdb.Connect(host = 'localhost', database= 'aulabd1',user = 'root', passwd = '')

cursor = cursor.cursor()
cursor.execute('SELECT * ')
pessoas = cursor.execute('SELECT * FROM pessoa')

def listar_todos(c):
    c.execute('SELECT * FROM pessoa')
    pessoas = c.fetchall()
    for p in pessoas:
        print(p)

def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)


listar_todos(cursor)

buscar_por_id(cursor,1)




