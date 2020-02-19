from Aula059.A59_Testes2 import Calc

class Teste:
    def teste_soma(self):
        objeto = Calc(5, 20)
        soma_objeto = objeto.soma()
        return soma_objeto

    def teste_multiplicacao(self):
        objeto = Calc(2,2)
        multiplicacao_objeto = objeto.multiplicacao()
        return multiplicacao_objeto

    def teste_subtracao(self):
        objeto = Calc(2,1)
        subtracao_objeto = objeto.subtracao()
        return subtracao_objeto


# criando a variavél "c", parta chmar a classe "Teste"
c = Teste()
#printano, o método "teste_soma()", da classe "Teste" que agora está contida na variavél "c"
print(c.teste_soma())
#---------------------------
print(c.teste_multiplicacao())
#-----------------------------
print(c.teste_subtracao())
