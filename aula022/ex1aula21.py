# Aula 21 - 09-12-2019
# Como Tratar e Trabalhar Erros!!!



#2 como metodos: receber salario, comprara, pagar divida

#3 Quando recebe aumenta o dinheiro na carteira.

#4 quando compra aumenta  os bens e diminui o dinheiro na carteira

#5 se comprara e não tiver dinheiro suficiente deve diminuir o dinheiro da carteira
# e aumentar a divida.

#6 para  pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) Atriutos de estado:dinheir na carteira, divida, bens


#1 crie uma classe cliente 
# deve ter Como atributos: codigo, cpf, nome, idade, sexo
class Cliente:
     #atributos
    def __init__ (self, codigo1, cpf1, nome1, idade1, sexo1):
        self.codigo = codigo1
        self.cpf = cpf1
        self.nome = nome1
        self.idade = idade1
        self.sexo = sexo1
     #atributos de estado
        self.dinheiro_c = 0
        self.divida = 0
        self.bens  = None

    def r_salario(self,trabalhou):
        self.dinheiro_c+=trabalhou
         
        

            

    def d_comprar(self,gastou):
        if gastou == True:
            self.dinheiro_c -= 900
            self.bens = 'Video Game'

    def pagar_d (self,pagar):
        if self.dinheiro_c >= 2000:
            self.dinheiro_c -= 700
        else:
            print('Sem saldo para pagar a divida')

 

pessoa1 = Cliente('100', '1125845', 'GABRIEL', 20, 'M')

pessoa1.r_salario(True)
pessoa1.d_comprar(True)
pessoa1.pagar_d(True)


pessoa1.r_salario(int(input('Digite um salário: ')))

print(f'dinheiro da carteira {pessoa1.dinheiro_c}\n')
print(f'valor da divida {pessoa1.divida}\n')
print(f'pagando divida {pessoa1.pagar_d}\n')

