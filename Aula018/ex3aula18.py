# Aula 18 - 03-11-2019

# A lista a seguir possui mais uma lista interna, a lista de preços.
# A lista de preços possui 3 sublistas dentro dela com os preços dos produtos.
# para exemplificar, o preço do mamão é de 10.00 - alface crespa é de 2.99 e o feijão 9.0

lista = [['frutas','verduras','legumes','preço'],
         ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
         ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha',],
         ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
         [ [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
           [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
         ]
        ]

# Será solicitado o preço de alguns produtos. para imprimir deve ser por f-string refrenciando o nome com o preço 
# da seguinte forma: "O preço do {} é R$ {}"

print('1: imprima o valor do abacaxi')
print(f'{lista[1][1]} Seu valor é de: {lista[4][0][0]}''\n')#o primeiro colchete aponta para qual lista o segundo colchetes aponta qual elemento da lista apontada eu quero

print('2: imprima o valor da rucula')
print(f'{lista[2][2]} Seu valor é de: {lista[4][0][1]} ''\n')

print('3: imprima o valor da laranja')
print(f'{lista[1][2]} Seu valor é de:{lista[4][0][2]}' '\n')

print('4: imprima o valor do repolho')
print(f'{lista[2][5]} Seu valor é de: {lista[4][1][0]}''\n')

print('5: imprima o valor do feijão')
print(f'{lista[3][0]} Seu valor é de {lista[4][0][3]}''\n')

print('6: imprima o valor do feijão branco')
print(f'{lista[3][4]} Seu valor é de: {lista[4][0][4]}''\n')

print('7: imprima o valor da vergamota')
print(f'{lista[1][6]} Seu valor é de: {lista[4][0][5]}''\n')

print('8: imprima o valor da alface lisa')
print(f'{lista[2][1]} Seu valor é de: {lista[4][1][1]}''\n')

print('9: imprima o valor do mamão')
print(f'{lista[1][0]} Seu valor é de: {lista[4][1][2]}''\n')

print('10: imprima o valor da soja')
print(f'{lista[3][6]} Seu valor é de: {lista[4][1][3]}''\n')

print('11: imprima o valor da lentilha')
print(f'{lista[3][2]} Seuvaloré de: {lista[4][1][4]}''\n')

print('12: imprima o valor da uva')
print(f'{lista[1][3]} Seu valor é de: {lista[4][1][5]}''\n')

print('13: imprima o valor da vagem')
print(f'{lista[3][3]} Seu valor é de: {lista[4][1][6]}''\n')

print('14: imprima o valor do almeirão')
print(f'{lista[2][3]} Seu valor é de: {lista[4][2][0]}''\n')

print('15: imprima o valor da ervilha')
print(f'{lista[3][1]} Seu valor é de: {lista[4][2][1]}''\n')

print('16: imprima o valor da maçã')
print(f'{lista[1][5]} Seu valor é de: {lista[4][2][2]}')