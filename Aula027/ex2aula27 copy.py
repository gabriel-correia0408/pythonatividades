# Aula 21 - 16-12-2019
#Operadores in is ==
#is

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)

# print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
print('Questão 1','\n')
if lista[0] is lista[1]:
    print(f'São a mesma')
elif lista[0] == lista[1]:
    print(f'São iguais')
else:
    print(f'Não são iguais')
    
print('---'*10)
print('\n')

# 2) Qual é o maior valor destas duas listas 
print('Questão 2','\n')
if max(lista[0]) > max(lista[1]):
    print(f'O maior número é: {max(lista[0])}')
else:
    print(f'O maior número é: {max(lista[1])} ')

print('---'*10)
print('\n')


# 3) Qual é o maior valor de cada lista
print('Questão 3','\n')
print(f'O maior valor da lista 1 é: {max(lista[0])}')
print(f'O maior número da lista 2 é: {max(lista[1])}')
print('---'*10)
print('\n')


# 4) Há o número 10 dentro da lista[0]?

# def encontrar(parametro):
#     lista_vazia = []
#     for i in range(len(lista[0])):
#         for (j) in (i):
#             if buscar in lista[i][j]:
#                 lista_vazia.append(i,j)

# en  = encontrar(10)

# print(en)
print('Questão 4','\n')
lista[0].append(10)

if 10 in lista[0]:
    print(f'Sim há o número 10 em lista[0]')
else:
    print('Não, tem o número 10 em lista[0]')

print(lista[0])
print('---'*10)
print('\n')




# 5) Há o número 20 dentro da lista[1]?
print('Questão 5','\n')
if 20 in lista[1]:
    print(f'Sim o número 20 está em lista[1]')
else:
    print(f'Não,tem o número 20 em lista[1] ')

print(lista[1])
print('---'*10)
print('\n')


# 6) Quantos números da lista[0] tem dentro da lista[1]?
print('Questão 6','\n')
contador = 0
for i in lista[0]:
    if i in lista[1]:
        contador = contador + 1

print(contador) 
print(lista[0])
print(lista[1])
print('---'*10)
print('\n')
        
    

    

# 7) Mostre os números da lista[0] que estão dentro da lista[1]
print('Questão 7','\n')
contador2 = 0
for i in lista[0]:
    for j in lista[1]:
        if i == j :
            contador2 += 1 
else:
    print('Não a numeros iguais')

print(f'lista zero:{lista[0]}','\n')
print(f'lista um:{lista[1]}','\n')
print(f'total:{contador2}','\n')
print('---'*10)
print('\n')

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]
print('Questão 8')
somar = sum(lista[0])
for i in lista[1]:
    print(f'{somar * i}','\n')
    
print('---'*10)
print('\n')


# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
print('Questão 9')
numero_maior = max(lista[1])
numero_menor  = min(lista[0])
divisao_inteira = (numero_maior / numero_menor)
print(f'{divisao_inteira}','\n')
print('---'*10)
print('\n')

# 10) Ferifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
maior = max(lista[0])
menor = min(lista[1])
print('Questão 10')
if maior in lista[1]:
    print(f'O maior número da lista [0]: {maior} está dentro da lista[1]')
    print(f'lista 1: {lista[1]}','\n')
elif maior not in lista[1]:
    print(f'o maior número da lista[0]: {maior} não está dentro da lista[1]')
if menor in lista[0]:
    print(f'O menor número da lista [1]: {menor} está dentro da lista[0]')
    print(f'lista 0: {lista[0]}','\n')
elif menor not in lista[0]:
    print(f'O menor número da lista [1]: {menor} não está dentro da lista[0]')
else:
    print('nenhum número foi encontrado''\n')





