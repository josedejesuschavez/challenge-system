from src.Domain.Users.token_repository import TokenRepository
from src.Infraestructure.Persistence.SQLAlchemy.Mapping.token import Token


class CreateToken(object):
    def __init__(self, id, token, user_name, repository: TokenRepository):
        self.id = id
        self.token = token
        self.user_name = user_name
        self.repository = repository


    def execute(self):
        token_created = Token()
        token_created.id = self.id
        token_created.token = self.token
        token_created.user_name = self.user_name
        self.repository.add(token_created)