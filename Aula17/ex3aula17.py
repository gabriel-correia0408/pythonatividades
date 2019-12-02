# exerciocio  3 
# Faaça um progrma que leia um número inteiro de 1 a 100 no teclado 
# mostre se voce acerto  ou 
# o numero digitado é maior ou menor.
# quando vpce acertar o programa deve ser finalizado


''' Digite um número de um a dez para começar
    OU DIGITE 0 PARA SAIR

'''
from random import randint
nu = randint(1,10)#lança um número aleaório, de acordo com paramatros dentro dos parenteses
numero = 0

while not numero == nu:
    numero = int(input('Digite um número: '))
    if numero > nu:
        print('O número é menor!')
    elif  numero < nu:
        print('O número é maior')
    else:# A condição final 
        print('WINS')
    
    
