from projeto.dao.base_dao import BaseDao
from projeto.model.pessoa import Pessoa

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__(Pessoa)
