from rest.users.get import getUsers

class users_register_blueprint:
    def __init__(self, app):
        self.app = app

    def register(self):
        self.app.register_blueprint(getUsers.blueprint)
        return self.app