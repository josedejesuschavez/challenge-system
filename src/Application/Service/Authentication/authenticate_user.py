import uuid

from flask_jwt_extended import create_access_token

from src.Application.Service.Authentication.create_token import CreateToken
from src.Domain.Users.token_repository import TokenRepository
from src.Domain.Users.user_repository import UserRepository
from src.Infraestructure.Persistence.SQLAlchemy.Mapping.user import User


class AuthenticateUser(object):

    def __init__(self, email, password, user_repository: UserRepository, token_repository: TokenRepository):
        self.email = email
        self.password = password
        self.user_repository = user_repository
        self.token_repository = token_repository

    def execute(self):
        user_request = User()
        user_request.user_name = self.email
        user_request.password = self.password
        if len(self.user_repository.is_user_valid(user_request)) > 0:
            access_token = create_access_token(identity=user_request.user_name)
            application_service_create_token = CreateToken(id=str(uuid.uuid4()),
                                                           token=access_token,
                                                           user_name=self.email,
                                                           repository=self.token_repository)
            application_service_create_token.execute()
            return access_token
        else:
            raise Exception("User not valid")