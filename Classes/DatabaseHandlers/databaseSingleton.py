
from sqlalchemy import create_engine

class Database(object):
    """one single database connection"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            # dialect+driver://username:password@host:port/database
            Database._instance.engine = create_engine('mysql+pymysql://root:1152104@localhost/pharmassistant')
            # Database._instance.engine = create_engine('mysql+pymysql://root:@localhost/pharmassistant')
            # engine = Database._instance.engine

        return cls._instance

    def __init__(self):
        self.engine = self._instance.engine