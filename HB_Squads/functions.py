from colors import color


def get_int(message):
    while True:
        try:
            n = int(input(message))
        except:
            print(color('Digite um numero interio valido', 'red'))
        else:
            return n


def get_programador(programadores):
    while True:
        i = 1
        for p in programadores:
            print(color(f'{i} - {p}', 'green'))
            i += 1

        try:
            if len(programadores) > 1:
                n = get_int(color('Escollha um programador: ', 'blue')) - 1
            else:
                n = 0
            p = programadores[n]
        except:
            print(color('Programador não válido!  Tente novamente', 'red'))
        else:
            programadores.remove(p)
            return p


def get_linguagem(linguagens):
    while True:
        i = 1
        for l in linguagens:
            print(color(f'{i} - {l}', 'green'))
            i += 1

        try:
            if len(linguagens) > 1:
                n = get_int(color('Escollha um programador: ', 'blue')) - 1
            else:
                n = 0
            l = linguagens[n]
        except:
            print(color('Linguagem não válido!  Tente novamente', 'red'))
        else:
            linguagens.remove(l)
            return l

def get_framework_front(framework_front):
    while True:
        i = 1
        for f in framework_front:
            print(color(f'{i} - {f}', 'green'))
            i += 1

        try:
            if len(framework_front) > 1:
                n = get_int(color('Escollha um programador: ', 'blue')) - 1
            else:
                n = 0
            f = framework_front[n]
        except:
            print(color('Framework Frontend não válido!  Tente novamente', 'red'))
        else:
            framework_front.remove(f)
            return f

def get_banco_de_dados(banco_de_dados):
    while True:
        i = 1
        for b in banco_de_dados:
            print(color(f'{i} - {b}', 'green'))
            i += 1

        try:
            if len(banco_de_dados) > 1:
                n = get_int(color('Escollha um programador: ', 'blue')) - 1
            else:
                n = 0
            b = banco_de_dados[n]
        except:
            print(color('Banco de dados não válido!  Tente novamente', 'red'))
        else:
            banco_de_dados.remove(b)
            return b


def valida_dados(vagas):
    for dado in vagas:

        if dado['programador'] == 'Nicole' and dado['framework_frontend'] == 'Vue':
            return False

        if dado['linguagem'] == 'Java' and dado['banco_de_dados'] != 'PostgreSQL':
            return False

        if dado['linguagem'] == 'Angular' and dado['banco_de_dados'] != 'MongoDb':
            return False

        if dado['programador'] == 'Mateus' and dado['linguagem'] != 'Python':
            return False

        if dado['programador'] == 'Mateus' and dado['banco_de_dados'] == 'MySqlServer':
            return False

        if dado['programador'] == 'Tiago' and dado['linguagem'] == 'PHP':
            return False

    return True









