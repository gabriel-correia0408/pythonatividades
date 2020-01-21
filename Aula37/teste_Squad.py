import sys
sys.path.append('C:/Users/900137/Desktop/pythonatividades/pythonatividades/Aula37')
from Controller.Squad_controler import EnderecoController
from Model.endereco import Endereco

end = Endereco()
end.logradouro = 'Rua dos Pombos123'
end.numero = '0'
end.complemento = 'casa muito engraçada'
end.bairro = 'sem nome'
end.cidade = 'gaspar'
end.cep = '11111-000'
end.id = 123

contr=  EnderecoController()
id_salvo = contr.salvar(end)