from colors import color, color_bg
from functions import get_int, get_programador, get_linguagem, get_framework_front, get_banco_de_dados, valida_dados

programadores = ['Mateus', 'Tiago', 'Nicole']

linguagens = ['Python', 'Java', 'PHP']
framework_front = ['React', 'Angular', 'Vue']
banco_de_dados = ['MySqlServer', 'PostgreSQL', 'MongoDb']



vagas = []

for i in range(3):
    dados = {}
    dados['programador'] = get_programador(programadores)
    dados['linguagem'] = get_linguagem(linguagens)
    dados['framework_frontend'] = get_framework_front(framework_front)
    dados['banco_de_dados'] = get_banco_de_dados(banco_de_dados)
    vagas.append(dados)
    print()
    print(color('=========================', 'yellow'))
    print()


print(vagas)

for a in vagas:
    print(color('=========================', 'blue'))
    print(color_bg(a['programador'], 'blue', 'yellow'))
    print(color(a['linguagem'], 'blue'))
    print(color(a['framework_frontend'], 'blue'))
    print(color(a['banco_de_dados'], 'blue'))
    print()


print(color('=========================', 'yellow'))
if valida_dados(vagas):
    print(color('Deu certo!', 'purple'))
else:
    print(color('Deu errado!', 'purple'))








