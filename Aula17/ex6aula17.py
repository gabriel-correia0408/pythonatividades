# Criar um programa para o cadastro do cliente
# Para cadastro de clientes deve pedir os seguintes dados:
# Codigo do cliente , CPF, nome completo,
# data de nascimento, Estadi,Cidade,cep,bairro,rua
#numero da casa,complemento.

#cod_Cliente = input('Codigo de cliente:')
# cpf = input('CPF cliente: ')

def cadastro_cliente():
    dados_cliente = ['codigo_cliente', 'CPF', 'nome_completo', 'data_de_nascimento', 'estado', 'cidade','cep', 'bairro', 'rua', 'numero_casa', 'complemento']
    lista = []#declarando lista


    for j in range(numero)#detrmina um intervalo , o começo o fim e um encremento,cso tenha só um ele se torna o final
        dicionario = {}#declarando dicionario, e dentro do for para toda vez que rodar ele zerar e não ficar duplicando o dicionário dentro da lista

        for i in dados_cliente:#usando o for não se precisa criar inúmeros inputs
            dicionario[i] = input(f'{i} : ')
        lista.append(dicionario)#adiciona o dicionario dentro da lista
    return lista

numero =int(input('Digite número de cadastros: '))

lista_cliente = cadastro_cliente(numero)

# Criar uma função para salvar em arquivo:

arquivo = open('clientes.txt','a')
for cliente in arquivo:
        cliente_chave = list(cliente.keys)
    for chaves in cliente
    salvar = f'{cliente['codigo_cliente'];}'


arquivo.write()

arquivo.close()
