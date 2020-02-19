valor_dinheiro = float(input('Digite o valor de dinheiro a ser calculado o seu juro composto'))
porcentagem = float(input('Digite a porcentagem de juros que irá ser adicionada no decorrer de um ano')) 
tempo = float(input('Digite o tempo que será feito seu investimneto em meses'))
cl_porcentagem = float(porcentagem*valor_dinheiro)/100
# print(f'o total é de  {cl_rentabilidade}')


# def rentabilidade ():
#     cl_rentabilidade = valor_dinheiro*(1+porcentagem)**tempo

#     return cl_rentabilidade


def porcentagem1 (a,b):
   # print(f'o valor que está sendo recebido dentro da função(n1) é : {n11}')
    cl_porcentagem = (a * b)/100
    
    return cl_porcentagem

ujuj = porcentagem1(valor_dinheiro,porcentagem)

print(ujuj)