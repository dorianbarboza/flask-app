from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from model import *
#from Class.helloworld import HelloWorld
#from Class.Artista import Artista
from user.create import NewUser, ViewUsers


AppInstanceFlask = Flask(__name__)
ApiInstanceRestful = Api(AppInstanceFlask)
AppInstanceFlask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
AppInstanceFlask.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dorian:dorian12345@localhost/app_bd'
DatabaseInstanceAlchemy = SQLAlchemy(AppInstanceFlask)

@AppInstanceFlask.route('/getall/')
def get_all():
    try:
        users = Usuario.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return(str(e))

@AppInstanceFlask.route('/getbyid/<ID_Usuario>/')
def get_by_id(ID_Usuario):
    try:
        user = Usuario.query.filter_by(ID_Usuario = ID_Usuario).first()
        return jsonify(user.serialize())
    except Exception as e:
        return(str(e))

@AppInstanceFlask.route('/adduser/')
def add_user():
    ID_Usuario = request.args.get('ID_Usuario')
    username = request.args.get('username')
    password = request.args.get('password')
    try:
        user=Usuario(
            ID_Usuario = ID_Usuario,
            username = username,
            password = password
        )
        DatabaseInstanceAlchemy.session.add(user)
        DatabaseInstanceAlchemy.session.commit()
        return "Book added. book id={}".format(user.ID_Usuario)
    except Exception as e:
	    return(str(e))


#ApiInstanceRestful.add_resource(HelloWorld, '/helloworld/')
ApiInstanceRestful.add_resource(NewUser, '/api/v1/user/new')
ApiInstanceRestful.add_resource(ViewUsers, '/api/v1/user/view')



if __name__ == '__main__':
    AppInstanceFlask.run(host = '127.0.0.1', debug = True, port = 8080)
