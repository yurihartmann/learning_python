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

from HBSIS.SmartFortwo import SmartFortwo

terminal = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe de serviço', 'Comissaria 1', 'Comissaria 2', 'Policial', 'Prisioneiro']
aviao =[]

smart_fortwo = SmartFortwo(terminal, aviao)

smart_fortwo.viagem_terminal_aviao('Piloto', 'Oficial 1')
smart_fortwo.viagem_aviao_terminal('Piloto')

smart_fortwo.viagem_terminal_aviao('Piloto', 'Oficial 2')
smart_fortwo.viagem_aviao_terminal('Piloto')

smart_fortwo.viagem_terminal_aviao('Chefe de serviço', 'Comissaria 1')
smart_fortwo.viagem_aviao_terminal('Chefe de serviço')

smart_fortwo.viagem_terminal_aviao('Chefe de serviço', 'Comissaria 2')
smart_fortwo.viagem_aviao_terminal('Chefe de serviço')

smart_fortwo.viagem_terminal_aviao('Chefe de serviço', 'Piloto')
smart_fortwo.viagem_aviao_terminal('Chefe de serviço')

smart_fortwo.viagem_terminal_aviao('Policial', 'Prisioneiro')
smart_fortwo.viagem_aviao_terminal('Piloto')

smart_fortwo.viagem_terminal_aviao('Chefe de serviço', 'Piloto')

smart_fortwo.mostra_situacao()
















