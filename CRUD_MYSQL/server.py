from flask import Flask, render_template, redirect, request
from crud_mysql.models.Cliente import Cliente
from crud_mysql.models.ClienteDAO import ClienteDAO

app = Flask(__name__)
cDAO = ClienteDAO()


@app.route('/cliente')
def listagem():
    return render_template('listagem.html', clientes = cDAO.ler_clientes())

@app.route('/cliente', methods=['POST'])
def salvar_cliente_post():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']

    if request.form['id'] == '':
        c = Cliente(nome, sobrenome, cpf, request.form['id'])
        cDAO.salvar_cliente(c)
    else:
        c = Cliente(nome, sobrenome, cpf, request.form['id'])
        cDAO.editar_cliente_by_id(c)
    return redirect('/cliente')


@app.route('/cliente/<string:id>')
def form_cliente(id):
    if id == 'novo':
        return render_template('form_cliente.html', cliente = None)
    else:
        cliente = cDAO.ler_cliente_by_id(id)
        if cliente == None:
            return redirect('/cliente/novo')
        else:
            return render_template('form_cliente.html', cliente = cliente)

@app.route('/cliente/deletar')
def deletar():
    id = request.args['id']
    cDAO.excluir_cliente_by_id(id)
    return redirect('/cliente')


app.run(port=80, debug=True)