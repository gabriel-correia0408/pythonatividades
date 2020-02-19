import sys
sys.path.append('C:/Users/900137/Desktop/PythonAulas/pythonatividades/Aula034/controller')
from controller.enderecoo_db import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)
    