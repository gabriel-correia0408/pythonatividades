# o resource serve para podermos fazer as quatro requisições http get put post delete
from flask_restful import Resource
# o request serve para fazer a requisão do json,para o código.
from flask import request


# importando da minha pasta "Aula042", da sub-pasta "dao", e do arquivo "estado_dao", a classe "EstadoDao"
from Aula042.dao.estado_dao import EstadoDao
# importando da minha pasta "Aula042", da sub-pasta "model", e do arquivo "estado_model", a classe "EstadoModel"
from Aula042.model.estado_model import EstadoModel


# Criando a classe "EstadoController" passando o parametro resource para poder fazer as 4 rewuisições http
class EstadoController(Resource):
    # criando um método ,passando o construtor __init__,que permite que a classe inicialize os atributos da classe
    def __init__(self):
        # criando uma varivél "dao" que recebera ou melhor será minha classse "EstadoDao"
        self.dao = EstadoDao()


    # é passado o valor "none"para quando for testado e caso tenha um valor none ele nã entra no if
    def get(self, id=None):
        # o if faz a pergunta de que se tiver "id" ou melhor um valor no id, ele entra na linha a baixo ,caso contrário não
        if id:
            # o reutrn vai mandar o "id" para  para a variavél dao que contém a classe EstadoDao,e ira aplicano no métdo "buscar_por_id"
            return self.dao.buscar_por_id()
        # caso como citado nas linha acima ,ele não entre no if, ele entra n alinha abaixo,que reotrnara o método listar_todos
        return self.dao.listar_todos()


    #criando o método post ,colocando o self nos parametros para fazer a ligação com os outros arquivos e classes
    def post(self):
        #criando a varivél "regiao", atribuindo a ele o request eo json
        #o request vai fazer a requisão ao json,que retornara os valores em dicionários
        #através do penaltima linha que chama o método "inserir", que está no arquivo estado_dao
        regiao = request.json['regiao']
        estado = request.json['estado']
        populacao = int(request.json['populacao'])
        #criando uma váriavél "estados", que recebera a classe EstadoModel que trará seus parametros e valores
        estados = EstadoModel(regiao, estado, populacao)
        #criando a variavél "msg", e atribuindo a ela ,o self para fazer a conexao
        # e poder chamarda pasta "dao" o método inserir, e aplicar esse método no seu parametro que no caso
        # é a variavél "estados" antes criado para receber os valores, para que sejam aplicados no método "inserir" para retornarem
        # como json
        msg = self.dao.inserir(estados)
        #retonando para a varivél "msg" todos os dádos já passados pelos métodos e tratados
        return msg


    #criando o método "put",passando  o self nos parametros para poder fazer a ligação com outras classes e arquivos
    def put(self):
        #criando uma várivél "regiao", eatribuindo a ela o request  eo json
        # o request faz a requisaõ ou chama do json,que por sua vez retona valores em dicionários
        # por meo da penultima linha de código desse método,que chama o método "atualizar" que está no arquivo estado_dao
        regiao = request.json['regiao']
        estado = request.json['estado']
        populacao = request.json['popolacao']
        # criando uma váriavél "estados", que recebera a classe EstadoModel que trará seus parametros e valores
        estados = EstadoModel(regiao, estado, populacao)
        # criando uma varivél msg, e atribuindo a ela, o self para fazer a conexao e poder chamar da pasta "dao" o método
        # "atualizar", e aplicar esse método no parametro passado que no caso é a varivél "estados",que foi criada para
        # receber eos valores para que sejam aplicados no método "atualizar",para retornarem como json
        msg = self.dao.atualizar(estados)
        # retonando para a varivél "msg" todos os dádos já passados pelos métodos e tratados
        return  msg

    #criando o método "delete",passando sel para fazer a conexao com os arquivos e suas classes
    def delete(self):
        # retornando ,através do self, para a pasta "dao",usando o método "delete", que ira apagar o parametro passado
        # no caso o id , e uma vez apagando o id, apaga todas as outr s colunas desse id
        return self.dao.delete(id)




