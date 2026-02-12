class DatabaseFactory:
    _engine = None
    db_url: str

    def __init__(self, db_url: str):
        self.db_url = db_url

    def create_engine(self):
        if DatabaseFactory._engine is None:
            from sqlalchemy import create_engine
            DatabaseFactory._engine = create_engine(self.db_url)
        return DatabaseFactory._engine

    def create_session(self):
        from sqlalchemy.orm import sessionmaker
        engine = self.create_engine()
        Session = sessionmaker(bind=engine)
        return Session()