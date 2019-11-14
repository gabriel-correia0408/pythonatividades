#---- Exercicio 2 - Dicionários
#---- Escreva um programa que leia os dados de 11 jogadores
#---- jogador: Nome, Posicao, Numero, Pernaboa
#---- Crie um dicionario para armezenar os dados
#---- Imprima todos os jogadores e seus dados

jogador = []
lista = []
for i in range(1,3):
    jogador.append(input(f'Digite o nome do jogador {i+1}: '))
    jogador.append(input(f'Digite  a posição do jogador {i+1}: '))
    jogador.append(input(f'Digite o número do jogador {i+1}: '))
    jogador.append(input(f'Digite a perna boa jogador {i+1}: '))  
    lista.append(jogador)
    
lista = (f"{jogador['Digite o nome do jogador']} - {jogador['Digite  a posição do jogador']} - {jogador['Digite o número do jogador']} - {jogador['Digite a perna boa jogador']}" )
