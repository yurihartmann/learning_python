from flask import Flask, request
from flask_restful import Api

from API_REST.controllers.bebida_controller import BebidaController

app = Flask(__name__)
api = Api(app)

api.add_resource(BebidaController, '/api/bebidas', endpoint='bebidas')
api.add_resource(BebidaController, '/api/bebidas/<int:id>', endpoint='bebida')

app.run(port=80, debug=True)