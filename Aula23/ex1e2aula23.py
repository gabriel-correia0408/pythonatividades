# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo


# 6) Crie um metodo que possa atualizar os dados do cliente (cod cliente (int)), 
# nome, idade (int), sexo, email, telefone). Este metodo devera alterar tbm o dado bruto para 
# que na hora de salvar o dado em um arquivo, o mesmo nao esteja desatualizado. 


# 1) Faça uma classe cliente que receba como parametro o dado bruto.
class Cliente:#criando a classe
    def __init__(self, dadobruto):#adicionando parametros

        self.dado_bruto =  dadobruto
        self.codigo = None
        self.nome = None
        self.idade  = None
        self.sexo = None 
        self.email = None
        self.telefone  = None

    def listar(self):#metodo litar

        lista = self.dado_bruto.strip().split(';')#colocando os dados dentro de lista , e cortanto e fatiando com strip e split
        self.codigo = int(lista[0])#colocando minha varivél antes definida para receber, int , e sua posição dos dados que agr estão contidos em lista
        self.nome = (lista[1])#adicionando a varivél 'nome',o valor da posição dos dados contidos em lista
        self.idade = int(lista[2])
        self.sexo = (lista[3])
        self.email = (lista[4])
        self.telefone  = (lista[5])

    def salvar(self,daddostotal):
        arquivo_cliente = open('arquivop.txt','w')#denominando nome do arquivo, eo  criando
        arquivo_cliente.write(daddostotal)#fazendo a leitura do arquivo txt, que está salvo na variável 'arquivo_clienetes'
        arquivo_cliente.close()#fechando o arquivo para que possa ser executado

    def atualizar(self):
        self.nome = input('Digite  o nome do cliente: ')
        self.idade = int(input('Digite a nnova idadde do cliente: '))
        self.sexo = input('Digigte o sexo do cliente: ')
        self.email = input('Digite o email do cliente: ')
        self.telefone = input('Digite o telefone do cliente: ')
        




cliente = Cliente(dadobruto)
cliente.listar()
cliente.salvar(dadobruto)#atribuindo a classe o parametro que vou ela vai receber, para o metodoto 'salvar' receber esses dados

print(f'{cliente.nome}, {cliente.idade}, {cliente.sexo}, {cliente.email}, {cliente.telefone} ')#printando os dados 
        

        



        

        


