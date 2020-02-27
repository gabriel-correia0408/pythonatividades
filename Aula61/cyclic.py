#criando uma classe de nome "Matriz"
class Matriz:
    #criando um método de nome "rotação"
    def rotação(self):
        #criando uma variavél de nome "A" que recebe uma lista com elementos dentro dela
        self.A = [3, 8, 9, 7, 6]
        #criando uma variavél de nome "B" que recebe um variavél com elementos dentro dela que são diferentes da variavél A
        self.B = [1, 2, 3, 4]
        #Criando uma variavél de nome "lista",que recebe o "int" para definir que oque vai ser inserido nela são números inteiros
        #e passando o "input" para poder permetir que algo seja inserido, oquie está entre as strings é simplismente a msg
        #intuitiva para auxiliar um possivél usuário
        self.lista = int(input('Digite qual lista vc quer\nlista 1 = [3, 8, 9, 7, 6]\nlista 2 = [1, 2, 3, 4]: '))
        #criando uma variavél de nome "r" que recebe o "int" para definir que são números inteiros o que seráq inserido nela
        #e colocando o "input" para fazer a chamada e permitir que algo no caso um número seja inserido
        self.r = int(input('Digite o número que quer que aconteça a rotação: '))
        #criando um "if" para a a varivél "lista" que caso o valor que foi escolhidp foi o  1 é adicionado a varivél "lista"
        #a variavél "A" que nela por sua vez contém um alista com determinados elementos
        if self.lista == 1:
            self.lista  = self.A
        #criando o "elif" ou seja se não for o número 1 dentro da variavél "lista"  e for o número 2 dentro da varivél
        #"lista" então é executado as próximas linhas
        elif self.lista == 2:
            #caso o que foi escolhido fo 2 a variavél "lista" irá receber  a varivél "B" que esta por sua vez contém uma lista
            #com determinados elementos
            self.lista = self.B
        # criando um for, ou seja para a variavél "i" do for recebe o "range" o range po r sui avez quando recebe somente um número
        # ele vai contar do zero até o número contido em range,e o valor de range é número que foi digitado
        # e armazenado na variavél "r"
        for i in range(self.r):
            #atribuinado o método "insert" adicionado na posição zero da lista, o indice -1 ,que equivale a ultima posicção de uma lista
            #fazendo assim todos os elementos andarem uma  casa,no sentido anti-horario
            self.lista.insert(0, self.lista[-1])
            #o método "pop" remove por posição como seu argumento() está vazio ele remove a primeira posicão, que por sua vez tem outra igual por causa
            # das linhas anteriores terem adcionados,fazem assim a lista não item duplicados
            self.lista.pop()
            #printando a váriavél lista para averiguar se está correto oque fo pedido para ser feito
        print(self.lista)








#user.name=GABRI


m = Matriz()
m.rotação()
