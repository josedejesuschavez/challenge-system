from src.Infraestructure.Persistence.SQLAlchemy.PostgreSQLEngine import PostgreSQLEngine


class EngineFactory(object):
    def __init__(self):
        self.engines = {}
        self.prepare_engines()

    def prepare_engines(self):
        self.engines['PostgreSQLEngine'] = PostgreSQLEngine()

    def make_engine(self, env):
        engine = self.engines['PostgreSQLEngine']
        return engine.execute()