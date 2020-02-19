# Aula 15 28/11/2019
# Manipulação de arquivos

def salvar_pessoa(pessoa_dic):
    arquivo  = open('arquivo.txt', 'a')
    arquivo.write(f"{pessoa_dic['nome']};{pessoa_dic['sobrenome']};{pessoa_dic['idade']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('arquivo.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome':lista_linha[0], 'sobrenome':lista_linha[1], 'idade':lista_linha[2]}
        lista.append(pessoa)
    arquivo.close()
    return lista

# nome = input('Digite seu nome: ')
# sobrenome = input('Digite o sobrenome :')
# idade = int(input('Digite sua idade :'))

# pessoa = {'nome':nome, 'sobrenome':sobrenome, 'idade':idade}
# salvar_pessoa(pessoa)
    


for p in ler():
    print(f"{p['nome']} - {p['sobrenome']} - {p['idade']} ")