from flask_restful import Resource
from flask import request
from API_REST.dao.bebida_dao import BebidaDao

class BebidaController(Resource):

    def __init__(self):
        self.dao = BebidaDao()

    def get(self, id=None):
        if id:
            return  self.dao.buscar_por_id(id)
        else:
            retorno = []
            for a in self.dao.listar():
                retorno.append(a)
            return retorno


    def post(self):
        nome = request.json['nome']
        teor = request.json['teor']
        id_tipo_bebida = request.json['tipo_bebida']

        id = self.dao.inserir(nome, teor, id_tipo_bebida)
        return self.dao.buscar_por_id(id)

    def put(self, id):
        nome = request.json['nome']
        teor = request.json['teor']
        tipo_bebida_id = request.json['tipo_bebida']
        self.dao.alterar(id, nome, teor, tipo_bebida_id)
        return "Alterado"

    def delete(self, id):
        self.dao.deletar(id)
        return "Deletado"
