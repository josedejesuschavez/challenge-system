from flask_jwt_extended import JWTManager

from src.Infraestructure.Web.Flask.app import create_app

app = create_app()
jwt = JWTManager(app)

if __name__ == "__main__":
    app.run()