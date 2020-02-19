import MySQLdb #---- Importando a biblioteca do banco de dados

def listar_todos():
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host = 'localhost',database='aulabd1', user='root', passwd='')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()
    #----- Criação do comando SQL e passado para o cursor
    comando_sql_select = "SELECT * FROM auladb1.tabela_enderecoo"
    cursor.execute(comando_sql_select)
    #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
    resultado = cursor.fetchall()
    return resultado
