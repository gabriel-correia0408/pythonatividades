# Aula 9 - 19/11/2019
#---- web2
# exercicio 3 aula 3

nome_completo = float(input('Digite seu nome completo:' ))
cpf = float(input('Digite seu cpf:' ))
num_registro = int(input('Digite seu número de registro:' ))
cargo = float(input('Digite seu cargo:' ))
salario = float(input('Digite seu salario:' ))
if(salario>0 and salario <= 1751.81):
    inss = salario * 0.08
elif (salario >1751.81 and salario <=2919.72) :
    inss = salario * 0.095
elif (salario >2919.72 and salario<=5839.45):
    inss = salario * 0.11
else:
    inss = 642.3395


irrf = 0
if(salario>1903.98 and salario <= 2826.65):
   irrf = salario * 0.095
elif (salario >2826.66 and salario <=3751.05) :
    irrf= salario * 0.15
elif (salario >3751.05 and salario<=4664.68):
  irrf = (salario - inss) * 0.225
elif(salario > 4664.68):
    irrf = (salario - inss)*0.275

salario_liquido = salario - inss - irrf

print(f'Seu salário liquido é {salario_liquido}')
print(f'Irrf: {irrf}' )
print(f'inss:  {inss}' )


