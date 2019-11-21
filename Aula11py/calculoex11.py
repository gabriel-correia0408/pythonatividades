# Importando a funçao/metodo para calculo do iss
from calculoiss import iss


#  #Criando função para o calculo de iss
# def iss (n11):
#    # print(f'o valor que está sendo recebido dentro da função(n1) é : {n11}')
#     cl_iss = (n11 * 5)/100
    
#     return cl_iss

#pedindio para o usuario digitar o valor do serviço e atribuir na variavél n1
valor_servico = float(input('Digite o valor do serviço'))

#chamando o metodo criado iss e adicionando o valor da variavél n1
valor_iss = iss(valor_servico)
servico_liquido = (valor_servico - valor_iss)
print(f'O valor liquido do seu serviço será de:  {servico_liquido} \n E o ISS cobrado foi  de: {valor_iss}')