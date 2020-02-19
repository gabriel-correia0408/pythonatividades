from Aula055.dao.base_dao import BaseDao
from Aula055.model.genero import Genero

class GeneroDao(BaseDao):
    def __init__(self):
        super().__init__(Genero)
