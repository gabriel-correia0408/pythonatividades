import MySQLdb #importando o banco de dados "MySQLdb"

from Aula42.estado_model import EstadoModel#importanta da pasta "Aula42" e do arqivo"estado_model" a classe"EstadoModel"

class EstadoDao:#Criando a classe dao aonde ira conter os métodos
    def __init__(self):#iniciando com  o construtar (__init__) ele é usado para inicializar o objeto para poder se criado a instancia
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019' )#criando a conexao com bd
        self.cursor =  self.connection.cursor()#definindo o cursor da conexao

    def listar_todos(self): # Criando método para listar todos da lista,do banco de dados
        self.cursor.execute("SELECT * FROM topskills01.ESTADOS")
        estados = self.cursor.fetchall() #o comando fetchall pega vários itens contidos na lista
        lista_estados = []  #declarando lista vazia para receber os dados
        for e in estados: #criando for e ,passando todos os valores contidos na variavél "estados" para a nova variavél ( e )
            estado = EstadoModel(e[1], e[2], e[3], e[0])# criando uma variavél "estado" aonde recebe a classe "EstadoModel"
            lista_estados.append(estado.__dict__) # adicionando na lista "lista_estados" através do metodo "append",
            #os valores que estão contidos em "estados"
        return lista_estados # retornando para  a lista "lista_estados"

    def buscar_por_id(self, id):#criando método "buscar_por_id", o parametro "self" faz a ligação, o id vem do arquivo estado_model
        self.cursor.execute("SELECT * FROM topskills01.ESTADOS WHERE ID = {}".format(id))#passando o "self.cursor"para fazer a conexao" eo "execute"para executar o comando anterior
        estado = self.cursor.fetchone()#criando uma variavél "estado" que equivale ao "self.cursor" que fera o fetchone=buscar um
        e = EstadoModel(estado[1], estado[2], estado[3], estado[0])#criando a variavél "e" para poder receber,os valores do EstadoModel, e buscar eles por posição
        return e.__dict__#um método do python que transfroma o valor em dicionário

    def inserir(self):#criando método inserir.
        self.cursor.execute("""INSERT INTO topskills01.ESTADOS    
                            (regiao, estado, populacao)
                            VALUES('{}', '{}', '{}')""".format(estado.regiao, estado.estado, estado.populacao))#pagando a varivél "estado"
                            #que contém os dados do bd, e adicioando ,através do comando INSERT... por parametro por ex:regiao populacao

    def atualizar(self, estado: EstadoModel):#Criando método para atualizar,passando o "EstadoModel" para trazer os parametros para se completar o código
        self.cursor.execute(""" UPDATE topskill01.ESTADOS 
                         SET
                             regiao
                             estado
                            populacao
                        WHERE ID = {}""".format(pessoa.nome, pessoa.sobrenome, pessoa.idade, pessoa.id))
        self.connection.commit()#passnado a conexao e salvando a atualização através commit
        return estado.__dict__ #passavdo os dados para dicionário através do "__dict__"

    def delete(self):#criando méto delete para apagar
        self.cursor.execute(""" DELETE FROM topskills01.ESTADOS WHERE ID = {}""".format(id) #passando comando do que e quero apagar


                                )