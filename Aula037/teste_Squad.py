contr=  EnderecoController()
id_salvo = contr.salvar(end)
import sys
sys.path.append('C:/Users/900137/Desktop/pythonatividades/pythonatividades/Aula037')
from Controller.pessoa_controller import PessoaController
from Model.pessoa import Pessoa

pessoa = Pessoa()
pessoa.nome = 'Draeta1'
pessoa.sobrenome = 'Lindao'
pessoa.idade = 49
pessoa.endereco.logradouro = 'Rua dos Pombos1'
pessoa.endereco.numero = '0'
pessoa.endereco.complemento = 'casa muito engraçada'
pessoa.endereco.bairro = 'sem nome'
pessoa.endereco.cidade = 'gaspar'
pessoa.endereco.cep = '11111-000'

controller = PessoaController()
#id_salvo = controller.salvar(pessoa)
#pessoa_endereco = controller.buscar_por_id(id_salvo)
#print(pessoa_endereco)
print(controller.buscar_por_id(1))