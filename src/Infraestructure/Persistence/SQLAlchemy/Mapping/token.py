from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from src.Infraestructure.Domain.Base import Base


class Token(Base):
    __tablename__ = 'tokens'

    id = Column(UUID(as_uuid=True), primary_key=True)
    token = Column(String(length=500))
    user_name = Column(String(length=50))