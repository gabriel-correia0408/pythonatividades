#---exercicio 1 dicionario
#----Escreva um programa que leia os dados de cerveja
#----- cerveja: Marca,tipo,ibu,abv,ebc, volume
#-----Imprima os dados dos dicionario(não dicionario completo)

lista = []
print('=='*50)
dicionario = {'Cerveja':input('Digite a marca: \n'), 'Tipo':input('Digite o tipo:\n'), 'IBU':input('ibu:\n'), 'ABV':input('abv:\n'), 'EBC':input('ebc\n'),'Volume':input('Digite o volume\n')}
print(lista)
print('=='*50)
lista = (f"{dicionario['Cerveja']} - {dicionario['Tipo']} - {dicionario['IBU']} - {dicionario['ABV']} - {dicionario['EBC']} - {dicionario['Volume']}")
print(lista)
