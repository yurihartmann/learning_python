class SmartFortwo:

    def __init__(self, terminal: list, aviao: list):
        self.terminal = terminal
        self.aviao = aviao

    def mostra_situacao(self):
        print('\033[1;35m')
        print(format(' SITUACAO ', '^60'))
        print('TERMINAL = ', self.terminal)
        print('AVIAO = ', self.aviao)
        print('\033[m')

    def viagem_terminal_aviao(self, p1, p2):
        self.mostra_situacao()
        self.terminal.remove(p1)
        self.terminal.remove(p2)
        print('\033[1;32m')
        print('Fortwo indo para o aviao = ', p1, ' e ', p2)
        print('\033[m')
        self.aviao.append(p1)
        self.aviao.append(p2)

    def viagem_aviao_terminal(self, p1, p2=None):
        self.mostra_situacao()
        self.aviao.remove(p1)
        if p2:
            self.aviao.remove(p2)
        print('\033[1;31m')
        print('Fortwo voltando para o aviao = ', p1, ' e ', p2)
        print('\033[m')
        self.terminal.append(p1)
        if p2:
            self.terminal.append(p2)
