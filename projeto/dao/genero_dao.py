from projeto.dao.base_dao import BaseDao
from projeto.model.genero import Genero

class GeneroDao(BaseDao):
    def __init__(self):
        super().__init__(Genero)
