'''

A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais.
A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial
junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima.
A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

Requisitos:
,
1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
5 - Utilizar funções em arquivo separado do executor terminal
6 - Deve ser feito apenas com biblioteca padrão do Python e em Console(Terminal)

'''

terminal = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe de serviço', 'Comissaria 1', 'Comissaria 2', 'Policial', 'Prisioneiro']
aviao =[]

def mostra_situacao():
    print('\033[1;35m')
    print(format(' SITUACAO ', '^60'))
    print('TERMINAL = ',  terminal)
    print('AVIAO = ', aviao)
    print('\033[m')

def viagem_terminal_aviao(p1, p2):
    mostra_situacao()
    terminal.remove(p1)
    terminal.remove(p2)
    print('\033[1;32m')
    print('Fortwo indo para o aviao = ', p1, ' e ', p2)
    print('\033[m')
    aviao.append(p1)
    aviao.append(p2)

def viagem_aviao_terminal(p1, p2=None):
    mostra_situacao()
    aviao.remove(p1)
    if p2:
        aviao.remove(p2)
    print('\033[1;31m')
    print('Fortwo voltando para o aviao = ', p1, ' e ', p2)
    print('\033[m')
    terminal.append(p1)
    if p2:
        terminal.append(p2)


viagem_terminal_aviao('Piloto', 'Oficial 1')
viagem_aviao_terminal('Piloto')

viagem_terminal_aviao('Piloto', 'Oficial 2')
viagem_aviao_terminal('Piloto')

viagem_terminal_aviao('Chefe de serviço', 'Comissaria 1')
viagem_aviao_terminal('Chefe de serviço')

viagem_terminal_aviao('Chefe de serviço', 'Comissaria 2')
viagem_aviao_terminal('Chefe de serviço')

viagem_terminal_aviao('Chefe de serviço', 'Piloto')
viagem_aviao_terminal('Chefe de serviço')

viagem_terminal_aviao('Policial', 'Prisioneiro')
viagem_aviao_terminal('Piloto')

viagem_terminal_aviao('Chefe de serviço', 'Piloto')

mostra_situacao()
