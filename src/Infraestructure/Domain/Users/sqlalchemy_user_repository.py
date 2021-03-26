import hashlib

from sqlalchemy.orm import sessionmaker

import settings
from src.Domain.Users.user_repository import UserRepository
from src.Infraestructure.Persistence.SQLAlchemy.Mapping.user import User


class SQLAlchemyUserRepository(UserRepository):

    def is_user_valid(self, user):
        password_encrypted = hashlib.md5(user.password.encode()).hexdigest()
        return self.session.query(User).filter_by(user_name=user.user_name, password=str(password_encrypted)).all()

    def __init__(self):
        session_maker = sessionmaker(settings.ENGINE)
        self.session = session_maker()

    def add(self, user):
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def update(self, user):
        self.session.commit()
        self.session.close()

    def delete(self, user):
        self.session.commit()
        self.session.close()

    def get_all(self):
        return self.session.query(User).all()