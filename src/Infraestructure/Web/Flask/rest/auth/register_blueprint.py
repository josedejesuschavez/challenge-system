from src.Infraestructure.Web.Flask.register_blueprint import RegisterBlueprint
from src.Infraestructure.Web.Flask.rest.auth.post import log_in, log_out


class AuthRegisterBlueprint(RegisterBlueprint):
    def __init__(self):
        pass

    def register(self, app):
        app.register_blueprint(log_in.blueprint, url_prefix='/auth')
        return app
