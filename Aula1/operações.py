nome = input('Digite seu nome:')
sb = input('Digite seu sobre nome:')
idade = int(input('Digite sua idade:'))
print(f'{nome} {sb}, tem {idade} anos')

if  idade < 18:
    print('Não pode beber bebida alcoolica') 
else:
    print('Ta começando agora vai devagar ')      