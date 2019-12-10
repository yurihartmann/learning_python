import sys

sys.path.append('C:/Users/900225/Desktop/python/TRABALHO')

from flask import Flask, render_template, redirect, request

from dao.linguagemDAO import LinguagemDAO
from model.linguagem import Linguagem

from dao.trabalhadorDAO import TrabalhadorDAO
from model.trabalhador import Trabalhador

from dao.equipeDAO import EquipeDAO
from model.equipe import Equipe


# INICIANDO O FLASK
app = Flask(__name__)

# INSTANCIANDO OS OBJETOS DE DAO
linguagemDAO = LinguagemDAO()
trabalhadorDAO = TrabalhadorDAO()
equipeDAO = EquipeDAO()


############## HOME ########################################################

@app.route('/')
def index():
    return "Home"

############## TRABALHADORES ########################################################

@app.route('/trabalhador')
def trabalhadores():
    # LISTA TODOS OS TRABALHADORES NUMA TABELA
    return render_template('trabalhador/listagem.html',
                           trabalhadores = trabalhadorDAO.listar(),
                           nav_item = 'trabalhador')


@app.route('/trabalhador/<string:id>')
def edicao_trabalhador(id):
    # VERIFICA SE TRATA DE UM NOVO OU APENAS EDICAO E FAZ A CHAMADA ADEQUADA
    if id == 'novo':
        return render_template('trabalhador/form.html',
                               trabalhador=Trabalhador('','','','','novo',''))
    else:
        return render_template('trabalhador/form.html',
                               trabalhador=trabalhadorDAO.dados_by_id(id))


@app.route('/trabalhador', methods=['POST'])
def salvar_trabalhador():
    # RECEBE TODOS OS CAMPOS DO FORMULARIO
    id_trabalhador =  request.form['id_trabalhador']
    id_pessoa =  request.form['id_pessoa']
    nome = request.form['nome_trabalhador']
    idade = request.form['idade']
    cargo = request.form['cargo']
    salario = request.form['salario']

    # TESTA SE PRECISA ALTUALIZAR UM ITEM OU ADICIONAR UM NOVO ITEM NO BANCO
    if id_trabalhador == 'novo':
        trabalhadorDAO.inserir(Trabalhador(nome, idade, cargo, salario))
    else:
        trabalhadorDAO.update(Trabalhador(nome, idade, cargo, salario, id_trabalhador, id_pessoa))

    # RETORNA PARA A LISTAGEM DOS TRABALHADORES
    return redirect('/trabalhador')


@app.route('/trabalhador/delete/<int:id_pessoa>/<int:id_trabalhador>')
def delete_trabalhador(id_pessoa, id_trabalhador):
    # RECEBE VIA ROTA OS ID PARA A EXCLUSAO DE UM TRABALHADOR
    trabalhadorDAO.delete(id_pessoa, id_trabalhador)
    return redirect('/trabalhador')

############## EQUIPES ########################################################

@app.route('/equipe')
def equipes():
    return render_template('equipes/listagem.html',
                           equipes = equipeDAO.listar(),
                           linguagemDAO = linguagemDAO,
                           nav_item = 'equipe')

@app.route('/equipe/<string:id>')
def edicao_equipe(id):
    # VERIFICA SE TRATA DE UM NOVO OU APENAS EDICAO E FAZ A CHAMADA ADEQUADA
    if id == 'novo':
        return render_template('equipes/form.html',
                               equipe = Equipe('','','novo'),
                               linguagens = linguagemDAO.listar())
    else:
        return render_template('equipes/form.html',
                               equipe = equipeDAO.dados_by_id(id),
                               linguagens = linguagemDAO.listar())


@app.route('/equipe', methods=['POST'])
def salva_equipe():
    # RECEBE OS DADOS DO FORMULARIO
    id = request.form['id']
    id_linguagem = request.form['id_linguagem']
    nome = request.form['nome_equipe']

    # TESTA SE PRECISA ALTERAR OU CRIAR UMA LINGUAGEM
    if id == 'novo':
        equipeDAO.inserir(Equipe(nome, id_linguagem))
    else:
        equipeDAO.update(Equipe(nome, id_linguagem, id))

    # RETORNA PARA A LISTAGEM DE LIGUAGENS
    return redirect('/equipe')




############## LINGUAGENS ########################################################

@app.route('/linguagem')
def lista_linguagens():
    return render_template('linguagens/listagem.html',
                           linguagens = linguagemDAO.listar(),
                           nav_item = 'linguagem')

@app.route('/linguagem/<string:id>')
def edicao_linguagem(id):
    # VERIFICA SE TRATA DE UM NOVO OU APENAS EDICAO E FAZ A CHAMADA ADEQUADA
    if id == 'novo':
        return render_template('linguagens/form.html',
                               linguagem = Linguagem('', 'novo'))
    else:
        return render_template('linguagens/form.html',
                               linguagem = linguagemDAO.dados_by_id(id))


@app.route('/linguagem', methods=['POST'])
def salva_linguagem():
    # RECEBE OS DADOS DO FORMULARIO
    id = request.form['id']
    nome = request.form['nome_linguagem']

    # TESTA SE PRECISA ALTERAR OU CRIAR UMA LINGUAGEM
    if id == 'novo':
        linguagemDAO.inserir(Linguagem(nome))
    else:
        linguagemDAO.update(Linguagem(nome, id))

    # RETORNA PARA A LISTAGEM DE LIGUAGENS
    return redirect('/linguagem')


@app.route('/linguagem/delete/<int:id>')
def delete_linguagem(id):
    # RECEBE VIA ROTA O ID PARA A EXCLUSAO DE UMA LINGUAGEM
    linguagemDAO.delete(id)
    return redirect('/linguagem')


######################################################################

app.run(debug=True, port=80)