import MySQLdb
from 2-Model.endereco import Endereco

class EnderecoDao:
    comexao = MySQLdb.connect(host= '',database='', user='', passwd='' )
    cursor = conaxao.cursor()

    def listar_todos(self):
        comando = SELECT *FROM f"01_MDG_ENDERECO WHERE ID = {id}"
        SELF.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        

    def buscar_por_id(self,id):
                comando = SELECT *FROM f"01_MDG_ENDERECO WHERE ID = {id}"
        SELF.cursor.execute(comando)
        resultado = self.cursor.fetchone()


    def salvar(self,endereco:Endereco):
         comando = """ INSERT INTO 01_MDG_PESSOA
         (
             NOME,
             SOBRENOME,
             IDADE,
             ID_ENDERECO




         )


         """
 

    def alterar(self,endereco:Endereco):
        comando = """
        """


    def deletar(self,id):
        COMANDO = F""" DELETE FROM 01_MSG_PESSOA WHERE ID = {id}
        """

