#======= Estruturas de dados e DB

#----- Importar biblioteca do Mysql
import MySQLdb
#----- Configurar a conexão
conexao = MySQLdb.connect(host = 'localhost',database='aulabd1', user='root', passwd='')
#----- Salva o cursor da conexão em uma variável
cursor = conexao.cursor()
#----- Criação do comando SQL e passado para o cursor
comando_sql_select = "SELECT * FROM aulabd1.pessoa"
cursor.execute(comando_sql_select)
#---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
resultado = cursor.fetchall()

#cria uma lista para armazenar os dicionarios
lista_pessoas = []
for p in resultado:
    #----- Criação do dicionario que representa uma pessoa
    dicionario_pessoa = {'id': 0, 'nome' : '', 'sobrenome': '', 'idade' : 0, 'id_endereco': 0}
    #--- pega cada posição da tupla e atribui a uma chave do dicionário
    dicionario_pessoa['id'] = p[0]
    dicionario_pessoa['nome'] = p[1]
    dicionario_pessoa['sobrenome'] = p[2]
    dicionario_pessoa['idade'] = p[3]
    dicionario_pessoa['id_endereco'] = p[4]
    lista_pessoas.append(dicionario_pessoa)

#----- Cria um arquivo e atribui a uma variável 'arquivo'
with open('33-Aula33/pessoas1.txt','a') as arquivo:
    #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
    for p in lista_pessoas:
        arquivo.write(f"{p['id']};{p['nome']};{p['sobrenome']};{p['idade']};{p['id_endereco']}\n")