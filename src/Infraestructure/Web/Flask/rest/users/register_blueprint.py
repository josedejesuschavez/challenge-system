from rest.users.get import log_in, log_out
from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
)


class UsersRegisterBlueprint:
    def __init__(self, app):
        self.app = app

    def register(self):
        self.app.register_blueprint(log_in.blueprint)
        self.app.register_blueprint(log_out.blueprint)
        self.app.register_blueprint(swaggerui_blueprint)
        return self.app