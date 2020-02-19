# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!
#

#iniciando a classe

class Cadastro:
    def __init__(self):
        self.lista=[]
        self.ler

    def ler(self):
        try:
9
            arquivo =open(f'arquivo2{nome}.txt', atributo)
            for pessoa in arquivo:
                pessoa = pessoa.strip().split(';') 
                # 1;Arnaldo;23;projeto;alexcabeludo2@hotmail.com;014908648117
                dic = {'codigo':pessoa[0], 'nome':pessoa[1], 'idade':pessoa[2],
                        'sexo':pessoa[3], 'email':pessoa[4], 'telefone':pessoa[5]}
                self.lista.append(dic)

        finally:#garamnte que o arquivo sejaafechado no final!!!!!!!!!!!
            arquivo.close()
    
    def salvar(self,atributo='a'):
        try:
            arquivo = open('arquivo2_novo.txt', 'a')
            for pessoa in self.lista:
                texto = (f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['email']};{pessoa['telefone']}")
        finally:
            arquivo.close()


    def cadastrar(self):
        ### codigo já retornados!!!
        nome = input('Digite o nome do cliente: ')
        idade = input('Digite a idade do cliente: ')
        sexo = input('Digite o sexo do cliente: ')
        email = input('Digite o email do cliente: ')
        telefone = input('Digite o telefone do cliente: ')

        codigo = str ( int(self.lista[-1]['codigo']) +1 )
        
        
        dic = {'codigo':codigo, 'nome':nome, 'idade':idade,
                'sexo':sexo, 'email':email, 'telefone':telefone}
        self.lista.append(dic)


    def consulta(self,codigo):
        for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:
                print(f'''
Codigo: {pessoa['codigo']}
Nome: {pessoa['nome']}
Idade: {pessoa['idade']}
Sexo: {pessoa['sexo']}
Email: {pessoa['email']}
Telefone: {pessoa['telefone']}
                ''')
                break

    def atualizar(self):
        for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:            
                nome = input('Digite o nome do cliente: ')
                idade = input('Digite a idade do cliente: ')
                sexo = input('Digite o sexo do cliente: ')
                email = input('Digite o email do cliente: ')
                telefone = input('Digite o telefone do cliente: ')
                # atualizar dados:
                pessoa['nome'] = nome
                pessoa['idade'] = idade
                pessoa['sexo'] = sexo
                pessoa['email'] = email
                pessoa['telefone'] = telefone

                self.salvar('arquivo2_novo.txt','w')


    # def salvar(self):
    #     arquivo = open('arquivo2.txt', 'r')#nest a linha contém o arquivo
    #     lista = []
    #     for linha in arquivo:
    #         linha = linha.strip().split(';')#aqui temo os dados formatados
    #         lista.append(linha)#adicionando todas as linhas, na lista antes definida vazia
    #     return lista

p = Cadastro()
# p.cadastrar()

p.consulta(20)

p.atualizar(20)

p.consulta(20)




# for i in range(20):
#     print(p.lista[i])

# ct = Cadastro()#defindo variavel que recebera aclasse, e a salvando
# cm = ct.salvar()#definindo variavel que recebe o metodo dentro da classe
# print(cm)
