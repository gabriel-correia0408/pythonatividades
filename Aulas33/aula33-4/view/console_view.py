import sys
sys.path.append('C:/Users/900137/Desktop/PythonAulas/pythonatividades/Aulas33')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)