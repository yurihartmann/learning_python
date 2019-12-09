from flask import Flask, render_template, redirect, request

app = Flask(__name__)


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

@app.route('/linguegens')
def linguegens():
    return 'linguegens'

app.run(debug=True, port=80)