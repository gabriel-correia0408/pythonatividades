# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!



# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# try:
#     print('Passou1')
#     numero = int(input('Digite um numero: '))
#     print('Passou2')
# except ValueError:
#     print('Voce digitou um numero erradp meu querido')
# else:
#     print('FIM')
#     break

#********************************************************#

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.
controle  = 'n'# atribuindo o valor 'n' a variavel   "controle"
while controle != 's':#while da o comando de != ele continua, se for igual ele encerra.
    try:#ele vai testar as próximas linhasdentro dele
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um segundo número: '))
    except ValueError:# caso try  tenha um erro ele irá, executar as linhas de códogo dentro do except
        print('Digite algo valido')
    else:#o else sempre executara indiferente de erro ou estar certo
        print(f'Soma entre {n1} e  {n2}  da um resultade de {n1+n2}')
        print(f'subtração entre {n1} e  {n2}  da um resultade de {n1-n2}')
        print(f' multiplicção entre {n1} e  {n2}  da um resultade de {n1*n2}')
    try :  # ele ira fazer uma nova verificaçaõ na linha a baixo caso tenha um erro ,ele ira para o próximo EXCEPT
        print(f' divisão entre {n1} e  {n2}  da um resultade de {n1/n2}')

    except ZeroDivisionError: #como o nome sugere não é divisivel por 0 
        print('lembrando não é possivel dividir por 0')   
       
    controle = input("Digite 's' para sair: ")# ADICIONANDO O VALOR A VARIVÉL

    if controle == 's':
        print('FIM')

        





###############################################################################################################################





