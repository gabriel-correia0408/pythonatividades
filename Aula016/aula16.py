# Aula 16 29-11-2019
#??????????

#cadastro de playlist
#lendo musica,artista e album


##################################  método   ######################################### 
# def criar_faixa(mus, alb, art):
#     faixa = {'musica': mus, 'album':alb, 'artista': art}




########################## importanto os métodos da faixa.py #########################
from faixa import criar_faixa, salvar_faixa, ler_faixa



    
#################################  variaveis #########################################
musica = input('Digite uma musica: ')
album = input('Digite o albúm: ')
artista = input('Digite o nome do artista: ')


################################# dicionário #########################################
# faixa = {'musica': musica, 'album':album, 'artista': artista}


#######################  chamando metodo,e definindo os parametros  ##################
faixa = criar_faixa(musica, album, artista)
salvar_faixa(faixa)

lista = ler_faixa()


for f in lista:
    print(f"{f['musica']} - {f['album']} - {f['artista']}")

############################ criando arquivo txt ################################ e adicionando com o write
# ----fechar arquivo = arquivo.close
# arquivo = open('faixas.txt','a')
# arquivo.write(f"{faixa['musica']};{faixa['album']};{faixa['artista']}")
# arquivo.close()