from sqlalchemy.orm import sessionmaker

import settings
from src.Domain.Users.token_repository import TokenRepository


class SQLAlchemyTokenRepository(TokenRepository):

    def __init__(self):
        session_maker = sessionmaker(settings.ENGINE)
        self.session = session_maker()

    def add(self, token):
        self.session.add(token)
        self.session.commit()
        self.session.close()

