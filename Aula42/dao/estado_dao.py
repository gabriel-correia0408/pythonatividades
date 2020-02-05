import MySQLdb #importando o banco de dados "MySQLdb"

from Aula42.estado_model import EstadoModel#importanta da pasta "Aula42" e do arqivo"estado_model" a classe"EstadoModel"
#Criando a classe dao aonde ira conter os métodos
class EstadoDao:
    # iniciando com  o construtar (__init__) ele é usado para inicializar o objeto para poder se criado a instancia
    def __init__(self):
        # criando a conexao com bd
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019' )
        # definindo o cursor da conexao
        self.cursor =  self.connection.cursor()

    # Criando método para listar todos da lista,do banco de dados
    def listar_todos(self):
        self.cursor.execute("SELECT * FROM topskills01.ESTADOS")
        # o comando fetchall pega vários itens contidos na lista
        estados = self.cursor.fetchall()
        # declarando lista vazia para receber os dados
        lista_estados = []
        # criando for e ,passando todos os valores contidos na variavél "estados" para a nova variavél ( e )
        for e in estados:
            # criando uma variavél "estado" aonde recebe a classe "EstadoModel"
            estado = EstadoModel(e[1], e[2], e[3], e[0])
            # adicionando na lista "lista_estados" através do metodo "append",os valores que estão contidos em "estados"
            lista_estados.append(estado.__dict__) # adicionando na lista "lista_estados" através do metodo "append",os valores que estão contidos em "estados"
        # retornando para  a lista "lista_estados"
        return lista_estados

        # criando método "buscar_por_id", o parametro "self" faz a ligação, o id vem do arquivo estado_model
    def buscar_por_id(self, id):
        # passando o "self.cursor"para fazer a conexao" eo "execute"para executar o comando anterior
        self.cursor.execute("SELECT * FROM topskills01.ESTADOS WHERE ID = {}".format(id))
        # criando uma variavél "estado" que equivale ao "self.cursor" que fera o fetchone=buscar um
        estado = self.cursor.fetchone()
        # criando a variavél "e" para poder receber,os valores do EstadoModel, e buscar eles por posição
        e = EstadoModel(estado[1], estado[2], estado[3], estado[0])
        # um método do python que transfroma o valor em dicionário
        return e.__dict__

    # criando método inserir.
    def inserir(self):
        # pagando a varivél "estado"que contém os dados do bd, e adicioando ,através do comando INSERT... por parametro por ex:regiao populaca
        self.cursor.execute("""INSERT INTO topskills01.ESTADOS    
                            (regiao, estado, populacao)
                            VALUES('{}', '{}', '{}')""".format(estado.regiao, estado.estado, estado.populacao))

    # Criando método para atualizar,passando o "EstadoModel" para trazer os parametros para se completar o código
    def atualizar(self, estado: EstadoModel):
        self.cursor.execute(""" UPDATE topskill01.ESTADOS 
                         SET
                             regiao
                             estado
                            populacao
                        WHERE ID = {}""".format(pessoa.nome, pessoa.sobrenome, pessoa.idade, pessoa.id))
        # passnado a conexao e salvando a atualização através commit
        self.connection.commit()
        # passavdo os dados para dicionário através do "__dict__"
        return estado.__dict__

        # criando méto delete para apagar
    def delete(self):
        self.cursor.execute(""" DELETE FROM topskills01.ESTADOS WHERE ID = {}""".format(id) #passando comando do que e quero apagar
                     )