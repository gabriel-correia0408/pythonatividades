class Matriz:
    def rotação(self):
        A = [1, 2, 3, 4]
        self.r = int(input('Digite o número que quer que aconteça a rotação: '))
        for i in range(self.r):
            A.insert(0, A[-1])
            A.pop()
        print(A)



m = Matriz()
m.rotação()

