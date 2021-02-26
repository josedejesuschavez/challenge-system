from flask_swagger_ui import get_swaggerui_blueprint
from src.Infraestructure.Web.Flask.register_blueprint import RegisterBlueprint
from src.Infraestructure.Web.Flask.rest.users.get import log_in, log_out

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




class UsersRegisterBlueprint(RegisterBlueprint):
    def __init__(self):
        pass

    def register(self, app):
        app.register_blueprint(log_in.blueprint)
        app.register_blueprint(log_out.blueprint)
        app.register_blueprint(swaggerui_blueprint)
        return app