# Aula 9 - 19/11/2019
#---
from aula_metodo import calculo_inss, calculo_irrf

salario  = float(input('Digite seu salario:' ))
inss = calculo_inss(salario)
irrf = calculo_irrf(salario,inss)


# nome_completo = input('Digite seu nome completo:' )
# cpf = input('Digite seu cpf:' ))
# num_registro = int(input('Digite seu número de registro:' ))
# cargo = input('Digite seu cargo:' )
# salario = float(input('Digite seu salario:' ))





salario_liquido = salario - inss - irrf

print(f'Seu salário liquido é {salario_liquido}')
print(f'Irrf: {irrf}' )
print(f'inss:  {inss}' )


