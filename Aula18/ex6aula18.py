# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"


# arquivo = open('cadastro.txt ', 'r')
# # conteudo  = arquivo.read()

# # lista_do_arquivo = conteudo.split('\n')


# # primerira_linha = linhas_do_arquivo[0]

# for linha in arquivo:  # a função for está ,andados oque há na variavel (arquivo) para a variavel do for 
    
#     campo = linha.strip().split(',')


#     contador  = 0
#     for campo in campos:
#         dicio[campo] = dados[contador]
#         i = i + 1

    # print(f'{campos[1]}: {campo[3]}')

def ler_cadastro():
    arquivo = open('cadastro.txt', 'r')
    print(arquivo)