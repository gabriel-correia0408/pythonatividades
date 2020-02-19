# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igual a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
#
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)

def lista_dic(lista_p):#criando a função,dando o parametro de 'lista_p'
        lista_dicionario = []#lista vazia para poder receber todos os dados e ser chamada no final
        for g in range(len(pess[0])):#vai me dar o começo '0' e  final '7'
                dicionario = {}#criando dicionário vazio,para depois poder adicionar nele
                for i in range(len(cab)): # range(4)
                    dicionario[cab[i]] = lista_p[i][g]#dicionario recebe os numos de elementos dentro do 'cab',que fica em 'i',
                    #o for irá ler as linhas em i, e os elementos em g.
                # dicionario = {'nome': lista_p[0][g], 'telefone': lista_p[1][g], 'email':lista_p[2][g], 'idade':lista_p[3][g] }
                if int(dicionario['idade']) >=18:#formula para resolver a questão
                    lista_dicionario.append(dicionario)#adicioando 

        return lista_dicionario#para retornar meu método
dados_total = lista_dic(pess)#colocando os elementos já tratados do meu método 'lista_dic', em uma variavél'dados_total

print(lista_dic(pess))#chamar meu método 'lista_dic' 'pess'

for qual in dados_total:# o qual recebe todos os elementos dentro de 'dados_total
    print(f'{qual}')#vai imprimir os elementos que agr estão dentro do 'qual'



         

