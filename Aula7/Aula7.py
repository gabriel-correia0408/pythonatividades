# Aula 7 - 14-11-2019
# Listas

lista = []
dicionario = {'chave':'valor' , 'chave':'valor' }
print(dicionario)


nome= 'Mirela'
lista_notas = [10,20,50,70]
media = sum(lista_notas)/ len(lista_notas)
situacao = 'Reprovado'
if media  >=7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome' :nome, 'listas_notas':lista_notas, 'Media': media, 'Situacao': situacao}

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['situacao']}")
