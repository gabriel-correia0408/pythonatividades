#print('Cadatramento do mercado tech')
#nomep = input('Digite o nome do produto: ')
#cat = input('Digite a categoria do produto: ')
#print(f'O produto é: {nomep} e sua categoria é: {cat}')




usuário = int(input('Digite 1 para cadastrar e 2 para sair: '))
lista = []

while usuário != 2:
    produto = input('Digite seus produtos: ')
    lista.append(produto)
    usuário = int(input('Digite 1 para cadstrar e 2 para sair: '))

print(lista)
