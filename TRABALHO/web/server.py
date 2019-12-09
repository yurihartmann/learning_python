from flask import Flask, render_template, redirect, request
from TRABALHO.dao.linguagemDAO import LinguagemDAO
from TRABALHO.model.linguagem import Linguagem

app = Flask(__name__)

linguagemDAO = LinguagemDAO()

############## HOME

@app.route('/')
def index():
    return "Home"

############## TRABALHADORES

@app.route('/trabalhadores')
def trabalhadores():
    return 'Trabalhadores'


############## EQUIPES

@app.route('/equipes')
def equipes():
    return 'equipes'

############## LINGUAGENS

@app.route('/linguagem')
def lista_linguagens():
    return render_template('linguagens/listagem.html', linguagens = linguagemDAO.listar())

@app.route('/linguagem/<string:id>')
def edicao_linguagem(id):
    if id == 'novo':
        return render_template('linguagens/form.html', linguagem = Linguagem('', 'novo'))
    else:
        return render_template('linguagens/form.html', linguagem = linguagemDAO.dados_by_id(id))


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