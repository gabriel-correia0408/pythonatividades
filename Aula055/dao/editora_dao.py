from Aula055.dao.base_dao import BaseDao
from Aula055.model.editora import Editora

class EditoraDao(BaseDao):
    def __init__(self):
        super().__init__(Editora)
