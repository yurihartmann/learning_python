from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://topskills03:Yuri2019@mysql.topskills.study/topskills03'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)


from controllers import EstudanteController

api.add_resource(EstudanteController, '/estudante', endpoint='estudantes')
api.add_resource(EstudanteController, '/estudante/<int:id>', endpoint='estudante')


# db.create_all()
app.run(port=80,debug=True)