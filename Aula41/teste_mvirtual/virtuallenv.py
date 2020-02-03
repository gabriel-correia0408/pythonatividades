from flask import Flask
from  flask_restful import Api

from controller.teste_controller import TesteAula

app = Flask(__name__)
api = Api(app)
api.add_resource(TesteAula, '/Api/Teste')


@app.route('/')
def inicio():
    return 'Teste de maquina virtuaal'

app.run(debug=True, port=80)
