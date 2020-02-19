from Aula055.dao.base_dao import BaseDao
from Aula055.model.pessoa import Pessoa

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__(Pessoa)
