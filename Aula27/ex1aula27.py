# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int


lista1 = lista_simples_int()
lista2 = lista_simples_int()
lista3 = lista_simples_int()


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(len(lista1))

# # 1.2) Qual é o maior valor da lista2?
print(max(lista2))

# # 1.3) Qual seria a soma do maior valor com o menor valor da lista2?

um = max(lista2)
dois = min(lista2)
rs = um + dois
print(f'O seu resultado é: {rs} ')


# # 1.4) Qual é a média aritmética da lista1?

td = sum(lista1)
tt = len(lista1)
total = td / tt
print(f'O seu resulatado será de {total}')

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)

t1 = sum(lista1)
t2 = sum(lista2)
t3 = sum(lista3)
print(f'A soma total da lista1 é de: {t1}' '\n' f'A soma total da lista2 é de: {t2}' '\n' f'A soma total da lista3 é de: {t3}')
som = t1 + t2 + t3
print(f'A soma total delas é de: {som}')




# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
for i  in lista1:
    print(f'{i}')


# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError

try:
    print(f'A posição das lista1, posição 5 é de: {lista1[5]} - A posição 9 é de: {lista1[9]} - Aposição 10 é de: {lista1[10]} - A posição 25 é de: {lista1[25]}')
    print(f'A posição das lista2, posição 5 é de: {lista2[5]} - A posição 9 é de: {lista2[9]} - Aposição 10 é de: {lista2[10]} - A posição 25 é de: {lista2[25]}')
    print(f'A posição das lista3, posição 5 é de: {lista3[5]} - A posição 9 é de: {lista3[9]} - Aposição 10 é de: {lista3[10]} - A posição 25 é de: {lista3[25]}')
except IndexError:
    pass


# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
lista_m = max(lista1, lista2, lista3)
if lista_m == lista1:
    print('A lista1 é a lista com mais itens')
elif lista_m == lista2:
    print('A lista2 é a lista com mais itens')
elif lista_m == lista3:
    print('A lista3 é a lista com mais itens')




# if len(lista1) > len(lista2) and len(lista1) > len(lista3):
#     print(f'A lista1 tem o maior número de itens sendo um total de: {len(lista1)}')
# elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
#     print(f'A lista2 tem o maio0r número de itens sendo um total de: {len(lista2)}')
# elif len(lista3) > len(lista1) > and len(lista3) > len(lista2):
#     print(f'A lista3 tem o maior  número de  itens sendo um total de: {len(lista)}')
# else:
#     print('As listas em questões tem o mesmo valor de itens')


# 1.9) Some os maiores números de todas as listas, e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.

soma = (max(lista1) + max(lista2) + max(lista3))
m1 = min(lista1)
m2 = min(lista2)
m3 = min(lista3)
if m1 < m2 and m3:
    print(soma - m1)
elif m2 < m1 and m3:
    print(soma - m2)
elif m3 < m1 and m2:
    print(soma - m3)


# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
l4 = (lista3 + lista2 + lista3)
print(max(l4) + min(l4))
