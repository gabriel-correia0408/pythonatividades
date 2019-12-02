def criar_faixa(musica, album, artista):
    faixa = {'musica': musica, 'album':album, 'artista': artista}
    return faixa

def salvar_faixa(faixa):
    arquivo = open('Aula16/faixas.txt','a')# o caminho para mandar para o arquivo onde o metodo sera chamado e xecutado
    arquivo.write(f"{faixa['musica']};{faixa['album']};{faixa['artista']}\n")
    arquivo.close()

def ler_faixa():
    arquivo = open('Aula16/faixas.txt','r')
    lista_faixas = [] #criar lista antes ou fora, do for para ela não ser limpa a cada leitura do for
    for linha in arquivo:
        linha =  linha.strip()#limpa o \n
        dados_faixa = linha.split(';')#retira todos os carctees dentro dos parenteses
        faixa = criar_faixa(dados_faixa[0], dados_faixa[1], dados_faixa[2]) #chamando metodo para criar dicionario para após chamar lista
        lista_faixas.append(faixa) #para adicionar ' faixa ', na lista 'lista_faixas
    arquivo.close()#linha de código para fechar o arquivo
    return lista_faixas #para retornar 'lista_faixas' e o for rodar em outro arquivo


