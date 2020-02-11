from projeto.dao.base_dao import BaseDao
from projeto.model.cliente import Cliente

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__(Cliente)