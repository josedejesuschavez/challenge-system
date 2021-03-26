from src.Infraestructure.Web.Flask.register_blueprint import RegisterBlueprint
from src.Infraestructure.Web.Flask.rest.pits.delete import delete_team_member
from src.Infraestructure.Web.Flask.rest.pits.get import get_team_members
from src.Infraestructure.Web.Flask.rest.pits.post import post_team_member
from src.Infraestructure.Web.Flask.rest.pits.put import put_team_member


class PitsRegisterBlueprint(RegisterBlueprint):
    def __init__(self):
        pass

    def register(self, app):
        app.register_blueprint(post_team_member.blueprint, url_prefix='/pits')
        app.register_blueprint(put_team_member.blueprint, url_prefix='/pits')
        app.register_blueprint(get_team_members.blueprint, url_prefix='/pits')
        app.register_blueprint(delete_team_member.blueprint, url_prefix='/pits')
        return app
