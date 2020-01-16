import sys
sys.path.append('C:/Users/900137/Desktop/PythonAulas/pythonatividades/Aula34')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)