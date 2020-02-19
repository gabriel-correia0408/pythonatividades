#criando a classe EstadoModel
class EstadoModel:
    # o "id" vai por ultimo ,pois ele tem uma valor pré-definido, os outros são meus parametros que tem no bd
    def __init__(self, regiao, estado, populacao,id=0):
        self.id = id
        self.regiao = regiao
        self.estado = estado
        self.populacao = populacao