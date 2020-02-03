import MySQLdb

from Aula42.estado_model import EstadoModel

class EstadoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019' )
        self.cursor =  self.connection.cursor()

    def listar_todos(self): # Criando método para listar todos da lista,do banco de dados
        self.cursor.execute("SELECT * FROM topskills01.ESTADOS")
        estados = self.cursor.fetchall() #o comando fetchall pega vários itens contidos na lista
        lista_estados = []  #declarando lista vazia para receber os dados
        for e in estados: #criando for e ,passando todos os valores contidos na variavél "estados" para a nova variavél ( e )
            estado = EstadoModel(e[1], e[2], e[3], e[0])# criando uma variavél "estado" aonde recebe a classe "EstadoModel"
            lista_estados.append(estado.__dict__) # adicionando na lista "lista_estados" através do metodo "append",
            #os valores que estão contidos em "estados"
        return lista_estados # retornando para  a lista "lista_estados"

    def buscar_por_id(self, id):
        self.cursor.execute("SELECT * FROM topskills01.ESTADOS WHERE  ")
