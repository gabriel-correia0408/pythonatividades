import MySQLdb
#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM pessoa')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)
        
#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM pessoa WHERE sobrenome like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade, id_endereco='NULL'):
    cr.execute(f"INSERT INTO pessoa (nome, sobrenome, idade, id_endereco) VALUES ('{nome}', '{sobrenome}',{idade},{id_endereco})")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id, nome, sobrenome, idade, id_endereco='NULL'):
    cr.execute(f"UPDATE pessoa SET nome='{nome}', sobrenome='{sobrenome}', idade={idade}, id_endereco={id_endereco} WHERE id={id} ")
    cn.commit()

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM pessoa WHERE id={id}')
    cn.commit()

# conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019' )
conexao  = MySQLdb.Connect(host = 'localhost', database= 'aulabd1',user = 'root', passwd = '')
cursor = conexao.cursor()

listar_todos(cursor)
buscar_por_id(cursor, 1)
buscar_por_sobrenome(cursor,'c')
salvar(conexao, cursor, 'Marcos', 'teste2', 2,3)
alterar(conexao, cursor, 20, 'TESTEZINHO', 'MUITOBOM', 1, 2)
deletar(conexao, cursor, 18)