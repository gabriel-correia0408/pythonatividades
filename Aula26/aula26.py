
a = 10
b = 10

print(id(a))
print(id(b))

a is b

a == b
lista = [0,1,2,3,4]
lista2 = lista
id(lista)
id(lista2)
lista is lista2
lista == lista2
lista.append(5)
lista_copia = lista.copy()
id(lista_copia)
id(lista)
lista_copia == lista
lista_copia is lista
lista_copia
lista

import copy