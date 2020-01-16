from model.enderecoo import Enderecoo
from dao.enderecoo_db import enderecoo_db

class PessoaController:
    p = Pessoa()
    p_db = enderecoo_db()

    def listar_todos(self):
        return self.p_db.listar_todos()

    def exportar(self):
        lpc = self.p_db.listar_todos()
        self.p.exportar_txt(lpc)