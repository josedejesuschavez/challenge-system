
import os

from sqlalchemy.ext.declarative import declarative_base

from src.Infraestructure.Persistence.SQLAlchemy.PostgreSQLEngine import PostgreSQLEngine

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'psycopg2',
        'NAME': 'challenge',
        'USER': 'challenge',
        'PASSWORD': '123qweQWE',
        'HOST': 'database',
        'PORT': 5432,
    }
}

engine_factory = PostgreSQLEngine()
ENGINE = engine_factory.execute(DATABASES['default'])

Base = declarative_base()