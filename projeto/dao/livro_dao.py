from projeto.dao.base_dao import BaseDao
from projeto.model.livro import Livro

class LivroDao(BaseDao):
    def __init__(self):
        super().__init__(Livro)
