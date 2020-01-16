def converter_tabela_dicionario(lista_tuplas):
    #cria uma lista para armazenar os dicionarios
    lista_pessoas = []
    for p in lista_tuplas:
        #----- Criação do dicionario que representa uma pessoa
        dicionario_pessoa = {'ID': 0, 'nome' : '', 'sobrenome': '', 'idade' : 0, 'id_endereco': 0}
        #--- pega cada posição da tupla e atribui a uma chave do dicionário
        dicionario_pessoa['id'] = p[0]
        dicionario_pessoa['nome'] = p[1]
        dicionario_pessoa['sobrenome'] = p[2]
        dicionario_pessoa['idade'] = p[3]
        dicionario_pessoa['id_endereco'] = p[4]
        lista_pessoas.append(dicionario_pessoa)
    return lista_pessoas