# --------------------- CLASSES -----------------
import MySQLdb #importando bilioteca mysql


def listar_todos():
    conexao = MySQLdb.connect(host = 'localhost',database='aulabd1', user='root', passwd='') #---configurar a conexao

    cursor =  conexao.cursor() #salvar o cursor em uma variavel

    lista_pessoas = []
    
    comando_sql_select = "SELECT * FROM  aulabd1.pessoa"  #criaçãp de um comando para o cursor mysql
    
    cursor.execute(comando_sql_select)# Pega todos os resultados da execução do comando SQL e armazena em uma variável
    
    resultado = cursor.fetchall()
    return resultado

def converter_dicionario():
    for p in resultado:
        dicionario_pessoa = {'id' : 0,'nome' : '', 'sobrenome': '', 'idade': 0, 'id_endereco':0} #dados de uma pessoa da tabela
        dicionario_pessoa['id'] = p[0]
        dicionario_pessoa['nome'] = p[1]
        dicionario_pessoa['sobrenome'] = p[2]
        dicionario_pessoa['idade'] = p[3]
        dicionario_pessoa['id_endereco'] = p[4]
        lista_pessoas.append(dicionario_pessoa)


def exportar_txt():


    
with open('pessoas.txt', 'a') as arquivo:
    for p in lista_pessoas:
        arquivo.write(f"{p['id']};{p['nome']};{p['sobrenome']};{p['idade']};{p['id_endereco']}\n")



    

    


