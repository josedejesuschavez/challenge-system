from sqlalchemy import create_engine


class PostgreSQLEngine(object):

    @staticmethod
    def execute(databases):
        settings_database = databases
        engine = settings_database['ENGINE']
        name = settings_database['NAME']
        user = settings_database['USER']
        password = settings_database['PASSWORD']
        host = settings_database['HOST']
        port = settings_database['PORT']

        return create_engine('postgresql+' + engine + '://' + user + ':' + password + '@' + host + ':' + str(port) + '/' + name
                             , pool_size=10, max_overflow=20)