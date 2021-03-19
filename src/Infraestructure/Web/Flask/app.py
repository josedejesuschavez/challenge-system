from flask import Flask
from flask_cors import CORS
from src.Infraestructure.Web.Flask.register_modules_blueprint import RegisterModulesBlueprint
from src.Infraestructure.Web.Flask.rest.users.register_blueprint import UsersRegisterBlueprint

        
def create_app():
    app = Flask(__name__)
    register_module = RegisterModulesBlueprint(app)
    register_module.append_module(UsersRegisterBlueprint())
    app = register_module.register()
    CORS(app)
    app.config["JWT_SECRET_KEY"] = "super-secret"
    return app