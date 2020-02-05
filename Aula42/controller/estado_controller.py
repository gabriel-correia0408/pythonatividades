# o resource serve para podermos fazer as quatro requisições http get put post delete
from flask_restful import Resource
# o request serve para fazer a requisão do json,para o código.
from Flask import  request



# importando da minha pasta "Aula42", da sub-pasta "dao", e do arquivo "estado_dao", a classe "EstadoDao"
from Aula42.dao.estado_dao import EstadoDao
# importando da minha pasta "Aula42", da sub-pasta "model", e do arquivo "estado_model", a classe "EstadoModel"
from Aula42.model.estado_model import EstadoModel


# Criando a classe "EstadoController" passando o parametro resource para poder fazer as 4 rewuisições http
class EstadoController(Resource):
    # criando um método ,passando o construtor __init__,que permite que a classe inicialize os atributos da classe
    def __init__(self):
        # criando uma varivél "dao" que recebera ou melhor será minha classse "EstadoDao"
        self.dao = EstadoDao()


    # é passado o valor "none"para quando for testado e caso tenha um valor none ele nã entra no if
    def get(self, id=None):
        # o if faz a pergunta de que se tiver "id" ou melhor um valor no id, ele entra na linha a baixo ,caso contrário não
        if id:
            # o reutrn vai mandar o "id" para  para a variavél dao que contém a classe EstadoDao,e ira aplicano no métdo "buscar_por_id"
            return self.dao.buscar_por_id()
        # caso como citado nas linha acima ,ele não entre no if, ele entra n alinha abaixo,que reotrnara o método listar_todos
        return self.dao.listar_todos()
