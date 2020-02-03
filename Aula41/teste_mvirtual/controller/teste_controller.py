from  flask_restful import Resource


class TesteAula(Resource):
    def __init__(self):
        self.connection = MySQLdb.connect(hodt='')

    def get(self): #get pega
        return 'teste aula 41,pega'

    def post(self): #post insere
        return  'teste aula 41 post,insere'

    def put(self): #put altera
        return  'teste aula 41 put,altera'

    def delete(self):
        return "teste aula41 delete ,apaga"


