class Pessoa:
    id = 0
    nome = ''
    sobrenome = ''
    idade = 0
    id_endereco = 0

    def exportar_txt(self, lista_pessoas):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('C:/Users/900137/Desktop/PythonAulas/pythonatividades/Aula34','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for p in lista_pessoas:
                arquivo.write(f"{str(p)}\n")
    
    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.id_endereco}'