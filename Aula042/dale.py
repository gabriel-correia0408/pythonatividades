# Chamando a biblioteca "flask",para importar o micro-fremework "Flask",que também pode ser a classe "Flask"
from  flask import  Flask
# Chamano a biblioteca "flask_restful",para trazer a classe "Api"
from flask_restful import Api

# Chamando a pasta "Aula042",da sub pasta "controller", arquivo "estado_controler", para importar  a classe "EstadoControlery"
from Aula042.controller.estado_controller import EstadoController

# Criando a variavél "app" que será minha aplicação, que recebe o Flask que por sua vez tem no parametro "__name__" por convenção
app = Flask(__name__)
#Criando a varivél  "api" que recebe, a classe "Api" que por sua vez recebe o parametro, "app", que foi criado nas linhas acima
api = Api(app)


api.add_resource(EstadoController, '/api/estado', endepoint = 'estados')
api.add_resource(EstadoController, '/api/estado', endepoint = 'estado')

app.run(debug=True)