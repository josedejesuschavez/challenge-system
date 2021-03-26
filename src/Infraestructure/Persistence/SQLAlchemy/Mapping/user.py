from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from src.Infraestructure.Domain.Base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_name = Column(String(length=50))
    password = Column(String(length=50))