nome = []
nota = []
n1 = 0
n2 = 1
n3 = 2
n4 = 3
for i in range(0,10):
    nome.append(input(f'Digite o nome do aluno {i+1}: '))
    for g in range(0,4):
        notas.append(float(input(f'Digite uma nota {g+1}:')))

for alunos in nome:
    meida = (nota[n0]+nota[n1]+nota[n2]+n3[n4])
resultado = 'Reprovado'
if media >=7:
    resultado = 'Aprovado'
print(f'Aluno: {nome[0]}- méida={meida} - Resultado: {resultado}' )

