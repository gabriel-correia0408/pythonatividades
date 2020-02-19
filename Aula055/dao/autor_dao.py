from Aula055.dao.base_dao import BaseDao
from Aula055.model.autor import Autor

class AutorDao(BaseDao):
    def __init__(self):
        super().__init__(Autor)