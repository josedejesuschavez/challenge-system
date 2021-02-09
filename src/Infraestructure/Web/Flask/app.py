from flask import Flask
from flask_cors import CORS
from Infraestructure.Web.Flask.rest.users.register_blueprint import UsersRegisterBlueprint
from abc import ABC, abstractmethod

class RegisterBlueprint(ABC):
    @abstractmethod
    def register(self, app):
        pass

class RegisterModulesBlueprint:
    def __init__(self, app):
        self.app = app
        self.modules_blueprints = []

    def append_module(self, module_blueprint):
        self.modules_blueprints.append(module_blueprint())

    def register(self):
        for module in self.modules_blueprints:
            self.app = module.register(self.app)

        return self.app
        
def create_app():
    app = Flask(__name__)
    register_module = RegisterModulesBlueprint(app)
    register_module.append_module(UsersRegisterBlueprint)
    app = register_module.register()
    CORS(app)
    return app