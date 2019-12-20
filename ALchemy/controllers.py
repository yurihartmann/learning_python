from flask_restful import Resource
from flask import jsonify, request, json

from models import Estudante

class EstudanteController(Resource):

    def get(self):
        a = []
        for e in Estudante.query.all():
            a.append(e.__str__())
        print(a)
        return a

    def post(self):
        nome = request.json['nome']
        e = Estudante(nome)
        Estudante.add(e)
        Estudante.commit()
        return "salvo"