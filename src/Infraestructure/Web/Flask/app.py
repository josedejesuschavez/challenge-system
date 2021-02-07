from flask import Flask
from flask_cors import CORS
from rest.users.register_blueprint import UsersRegisterBlueprint


def pool_register_blueprint(app):
    app = UsersRegisterBlueprint(app).register()
    return app

def create_app():
    app = Flask(__name__) 
    CORS(app)
    app = pool_register_blueprint(app)
    return app