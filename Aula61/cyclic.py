
class Matriz:
    def rotação(self):
        self.A = [3, 8, 9, 7, 6]
        self.B = [1, 2, 3, 4]
        self.lista = int(input('Digite qual lista vc quer\nlista 1 = [3, 8, 9, 7, 6]\nlista 2 = [1, 2, 3, 4]: '))
        self.r = int(input('Digite o número que quer que aconteça a rotação: '))
        if self.lista == 1:
            self.lista  = self.A
        elif self.lista == 2:
            self.lista = self.B

        for i in range(self.r):
            self.lista.insert(0, self.lista[-1])
            self.lista.pop()
        print(self.lista)








#user.name=GABRI


m = Matriz()
m.rotação()
