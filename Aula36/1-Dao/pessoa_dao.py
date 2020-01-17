import MySQLdb
from 2-Model.pessoa import Pessoa

class PessoaDao:
    comexao = MySQLdb.connect(host= '',database='', user='', passwd='' )
    cursor = conaxao.cursor()

    def listar_todos(self):
        pass

    def buscar_por_id(self,id):
        pass

    def salvar(self,pessoa:Pessoa):
         comando = """ INSERT INTO 01_MDG_PESSOA
         (
             NOME,
             SOBRENOME,
             IDADE,
             ID_ENDERECO




         )


         """

    def alterar(self,pessoa:Pessoa):
        pass

    def deletar(self,id):
        pass


