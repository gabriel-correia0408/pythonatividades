from flask import request
from Aula055.controller.base_controller import BaseController
from Aula055.dao.autor_dao import AutorDao
from Aula055.model.autor import Autor

class AutorController(BaseController):
    def __init__(self):
        dao = AutorDao()
        super().__init__(dao)

    def post(self):
        return super().post(self.carrega_parametros())

    def put(self, id):
        model = self.carrega_parametros()
        model.id = id
        return super().put(model)

    def carrega_parametros(self):
        model = Autor()
        model.pseudonimo = request.json['pseudonimo']
        model.descricao = request.json['descricao']
        model.pessoa_id = request.json['pessoa_id']
        return model