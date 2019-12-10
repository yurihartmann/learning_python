from flask import Flask, render_template, redirect, request
from TRABALHO.dao.linguagemDAO import LinguagemDAO
from TRABALHO.model.linguagem import Linguagem
from TRABALHO.dao.trabalhadorDAO import TrabalhadorDAO
from TRABALHO.model.trabalhador import Trabalhador


# INICIANDO O FLASK
app = Flask(__name__)

# INSTANCIANDO OS OBJETOS DE DAO
linguagemDAO = LinguagemDAO()
trabalhadorDAO = TrabalhadorDAO()


############## HOME

@app.route('/')
def index():
    return "Home"

############## TRABALHADORES

@app.route('/trabalhador')
def trabalhadores():
    return render_template('trabalhador/listagem.html',
                           trabalhadores = trabalhadorDAO.listar(),
                           nav_item = 'trabalhador')


@app.route('/trabalhador/<string:id>')
def edicao_trabalhador(id):
    if id == 'novo':
        return render_template('trabalhador/form.html',
                               trabalhador=Trabalhador('','','','','novo',''))
    else:
        return render_template('trabalhador/form.html',
                               trabalhador=trabalhadorDAO.dados_by_id(id))


@app.route('/trabalhador', methods=['POST'])
def salvar_trabalhador():
    id_trabalhador =  request.form['id_trabalhador']
    id_pessoa =  request.form['id_pessoa']
    nome = request.form['nome_trabalhador']
    idade = request.form['idade']
    cargo = request.form['cargo']
    salario = request.form['salario']

    if id_trabalhador == 'novo':
        trabalhadorDAO.inserir(Trabalhador(nome, idade, cargo, salario))
    else:
        trabalhadorDAO.update(Trabalhador(nome, idade, cargo, salario, id_trabalhador, id_pessoa))

    return redirect('/trabalhador')


@app.route('/trabalhador/delete/<int:id_pessoa>/<int:id_trabalhador>')
def delete_trabalhador(id_pessoa, id_trabalhador):
    trabalhadorDAO.delete(id_pessoa, id_trabalhador)
    return redirect('/trabalhador')

############## EQUIPES

@app.route('/equipes')
def equipes():
    return 'equipes'

############## LINGUAGENS

@app.route('/linguagem')
def lista_linguagens():
    return render_template('linguagens/listagem.html',
                           linguagens = linguagemDAO.listar(),
                           nav_item = 'linguagem')

@app.route('/linguagem/<string:id>')
def edicao_linguagem(id):
    if id == 'novo':
        return render_template('linguagens/form.html',
                               linguagem = Linguagem('', 'novo'))
    else:
        return render_template('linguagens/form.html',
                               linguagem = linguagemDAO.dados_by_id(id))


@app.route('/linguagem', methods=['POST'])
def salva_linguagem():
    id = request.form['id']
    nome = request.form['nome_linguagem']

    if id == 'novo':
        linguagemDAO.inserir(Linguagem(nome))
    else:
        linguagemDAO.update(Linguagem(nome, id))

    return redirect('/linguagem')


@app.route('/linguagem/delete/<int:id>')
def delete_linguagem(id):
    linguagemDAO.delete(id)
    return redirect('/linguagem')

app.run(debug=True, port=80)