from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900137/Desktop/PythonAulas/pythonatividades/Aula034')
from controller.enderecoo_controller import PessoaController

app = Flask(__name__)
pc = PessoaController()

@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    return render_template('index.html', lista = pessoas)

app.run()