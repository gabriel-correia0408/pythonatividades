#Importando da biblioteca "datetime" o método "datatime",que serve para buscar a hora do pc
from datetime import datetime
#criando uma varivél "dados",que recebe o parametro "dict" que ira converter os dados em dicionario
dados = dict()
#crinado a variavél
dados_n ['nome'] = str(input('Digigte seu  Nome'))
data_nasc = int(input('Digite sua data de nascimento'))
dados_i  ['Idade'] = datetime.now().year - data_nasc
dados ['genero'] = str(input('Digite se genero'))


print(dados)