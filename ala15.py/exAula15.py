def salvar_bebida (bebida_dic):
    arquivo = open('exarquivo.txt', 'a')
    arquivo.write(f"{bebida_dic['cerveja']};{bebida_dic['marca']};{bebida_dic['teor']};{bebida_dic['tipo']}")
    arquivo.close()

def ler_bebida():
    listab = []
    arquivo = open('exarquivo.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        linha_lista = linha.split(';')
        bebida = {'cerveja':linha_lista[0], 'marca':linha_lista[1], 'teor':linha_lista[2], 'tipo':linha_lista[3]}
        listab.append(bebida)
    arquivo.close()
    return listab


cerveja = input('Digite o nome da cerveja: ')
marca = input('Digite a marca: ')
teor = (input('Digite o teor: '))
tipo = input('Digite o tipo: ') 
bebida = {'cerveja':cerveja, 'marca':marca, 'teor':teor, 'tipo':tipo }
salvar_bebida(bebida)

for b in ler_bebida():
    print(f"{b['cerveja']} - {b['marca']} - {b['teor']} - {b['tipo']}")
