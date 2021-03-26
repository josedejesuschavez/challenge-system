import settings
from sqlalchemy import create_engine


class SQLiteEngine(object):

    @staticmethod
    def execute():
        return create_engine('sqlite:///' + settings.BASEDIR)