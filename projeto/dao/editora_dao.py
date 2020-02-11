from projeto.dao.base_dao import BaseDao
from projeto.model.editora import Editora

class EditoraDao(BaseDao):
    def __init__(self):
        super().__init__(Editora)
