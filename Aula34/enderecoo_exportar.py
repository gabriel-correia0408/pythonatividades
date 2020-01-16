def exportar_txt(lista_pessoas):
    #----- Cria um arquivo e atribui a uma variável 'arquivo'
    with open('C:/Users/900137/Desktop/PythonAulas/pythonatividades/Aula34/pessoas3.txt','a') as arquivo:
        #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
        for p in lista_pessoas:
            arquivo.write(f"{p['id']};{p['nome']};{p['sobrenome']};{p['idade']};{p['id_endereco']}\n")
