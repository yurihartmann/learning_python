from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(Flask(__name__))

class Estudante(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"<Estudante {self.nome}>"


