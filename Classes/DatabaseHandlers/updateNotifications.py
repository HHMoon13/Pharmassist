from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.create_table as create_table
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase

def update():
    Base = declarative_base()

    databaseInstance = SingletonDatabase.Database()
    engine = databaseInstance.engine

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    m = session.query(create_table.Notifications).filter(create_table.Notifications.status == 'unread').all()
    for i in m:
        i.status = 'read'
        session.commit()
        session.close()
