#for para dicionários

dias_de_cada_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# mes_e = int(input('Digite o me sem que você está(1 á 12): '))
# print('O mês', {mes_e}, 'tem',dias_de_cada_mes[mes_e], 'dias')

# print('Dias que faltam para acabar o ano, a partir do mes informado: ')
# print(sum(list(dias_de_cada_mes.values())[mes_e-1:]))


# total = 0
# for mes in range(mes_e, 12+1):
#     total += dias_de_cada_mes[mes]
# print('modo estruturado')
# print('total de dias até o final do ano', total)

for chave in dias_de_cada_mes:
    print('tenho uma chave nessa linha', chave)
    print('tenho uma chave nessa linha', dias_de_cada_mes[chave])

for chave, valor in dias_de_cada_mes.items():
    print('Para a chave', chave, 'O valor', valor)

# tupla = ('texto', 42, 5.01, int, str, list)#tupla composta varios tipo de dados
tupla = ('texto', 'texto de novo', 'tesstooo')
for isto in tupla:
    print(type(isto))