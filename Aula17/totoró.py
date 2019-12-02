# Aula 17 02/12/2019
#  o programa deve ter um menu interativo com um cabeçalho ,local para: Cadastro de clientes.
# rver clientes cadastrados,cadastrar produtos,ver produtos
# rlatórios de vendas eopção sair.
# Este menu deve se repetir até a opção sair for chamada.

menu = '''
##################################################################################################################
 #                           FESYIVAL DE TORORÓ                                                                  #
##################################################################################################################

1 - Cadastro de cliente
2 - ver clientes cadastrados
3 - Cadastro de produtos
4 - ver produtos cadastrados
5 - vendas
6 - relatório de vendas
7 - sair

Digite a opção desejada: '''
#com a opçaão input , 'opcao  = menu ' com o laço de repetição torna o menu interativo
while True:#com while a condição pode ser verdadeira(true) ou falça (false)
    opcao = input(menu)
    if opcao ==  '1':
        print('Cadastrar Clientes: ')
    elif opcao == '2':
        print('ver clientes cadastrados: ')
    elif opcao == '3':
        print('Cadastrar produtos')
    elif opcao == '4':
        print('Ver produtos cadastrados: ')
    elif opcao == '5':
        print('Vendas')
    elif  opcao == '6':
        print('Relatório de vendas: ')
    elif opcao == '7':
        print('sair')
    break
else:
    print('valor invalido')



