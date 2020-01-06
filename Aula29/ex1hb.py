# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo ás regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

aviao  = []
terminal = ['Piloto','oficial1','Oficial2','Chefe','Comissaria1','Comissaria2','Policial','Presidiário']
for a in range(1):
    print('\nSMARTWO saiu para buscar dois passageiros: ')
    aviao.append(terminal[0])
    aviao.append(terminal[1])
    terminal.pop(0)
    terminal.pop(0)
    print(f'\nEstão juntos no avião o {aviao[0]} e {aviao[1]}')
    print(f'\nO Smartwo saiu para buscar o passageiro nele está o motorista: {aviao[0]}, ele volta e fica no terminal')
    print(f'\nAtualamente estão no terminal {terminal}')
    # aviao = Piloto oficial1               oficial1[0] comissaria1 [1] 
    # Oficial2', 'Chefe', 'Comissaria1', 'Comissaria2', 'Policial', 'Presidiário'
    terminal.append(aviao[0])
    aviao.pop(0)
    aviao.append(terminal[1])
    aviao.append(terminal[2])
    terminal.pop(1)
    terminal.pop(1)
    #'oficial1', 'Chefe', 'Comissaria1']
    # 'Oficial2', 'Comissaria2', 'Policial', 'Presidiário', 'Piloto']
    print(f'\nNa ultima viagem chegaram ao avião: {aviao[1]} e {aviao[2]}')
    print(f'\nO Smartwo saiu para buscar um passageiro nele está o motorista: {aviao[1]}')
    print(f'\nAtualamente estão no terminal {terminal}')
    terminal.append(aviao[1])
    aviao.pop(1)
    aviao.append(terminal[4])
    aviao.append(terminal[5])
    terminal.pop(4)
    terminal.pop(4)
    
    print(f'\nE estão no momento dentro do avião {aviao}')
    print(f'\nE estão no momento no terminal {terminal}')
    # #aviao = oficial[0],comissaria[1], piloto[2],chefe[3]
    terminal.append(aviao[2])
    aviao.pop(2)
    aviao.append(terminal[1])
    aviao.append(terminal[4])
    terminal.append(aviao[2])
    aviao.pop(2)
    terminal.pop(4)
    terminal.pop(1)
    # terminal.append()
    print(f'\nE estão no momento dentro do avião {aviao}')
    print(f'\nE estão no momento no terminal {terminal}')
    aviao.append(terminal[1])
    aviao.append(terminal[2])
    terminal.pop(1)
    terminal.pop(2)
    print(f'Estão no momento no avião {aviao}')
    print(f'\nE estão no momento no terminal {terminal}')




# print(aviao)
# print(terminal)


        