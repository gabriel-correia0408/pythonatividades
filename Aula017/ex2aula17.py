# 1- Faça um menu interativo que tenha: Cadastro da banda,cadastro
# do album,cadastro da musica sair.
# O menu deve ser executado até que se escolha a opção sair.
#cada opção deve ser mostrada
#informações das bandas cadastradas,
#albuns e musicas

menu =  '''
########################################################################################################
###################################   Menu Bandas  #####################################################
########################################################################################################

1 - Cadastro de banda
2 - cadastro de album
3 - Cadastro da musica
4 - Sair

Digite uma opção: '''


l_banda =  []
l_album = []
l_musica = []
while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de bandas')
        cb = input('Digite a banda: ')
        l_banda.append(cb)
        print('Pronto')

    elif opcao == '2':
        print('Cadastro do album')
        ca = input('Digite o album: ')
        l_album.append(ca)
        print('Pronto')

    elif opcao == '3':
        print('Cadastro de musica')
        cm = input('Digite uma musica: ')
        l_musica.append(cm)
        print('Pronto')
    
    elif opcao == '4':
        print('Sair')
        break
    else:
        print('opção invalida')

print(f'Bandas cadastradas: {l_banda}')
print(f'Albums cadastrados: {l_album}')
print(f'Musicas cadastradas: {l_musica}')




