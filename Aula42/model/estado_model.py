class EstadoModel:#criando a classe EstadoModel
    def __init__(self, regiao, estado, populacao,id=0):#o "id" vai por ultimo ,pois ele tem uma valor pré-definido
        self.id = id
        self.regiao = regiao
        self.estado = estado
        self.populacao = populacao