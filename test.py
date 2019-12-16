#----Calculando média de alunos
nome = []
nota = []
n1 = 0
n2 = 1
n3 = 2
n4 = 3
for i in range(0,3):
    nome.append(input(f'Digite o nome do aluno {i+1}: '))
    for g in range(0,4):
        nota.append(float(input(f'Digite uma nota {g+1}: ')))

for alunos in nome:
    media = (nota[n1]+nota[n2]+nota[n3]+nota[n4]/4)
resultado = 'Reprovado'
if media >=7:
    resultado = 'Aprovado'
print(f'Aluno: {nome[0]}- média={media}- Resultado: {resultado}')


#arrumar este programa para que mostre o resultad dos três alunos
#na tela.


# while para que serve e como usar ele 
