from Classes.DatabaseHandlers import addPattern as Factory
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase
import Classes.DatabaseHandlers.create_table
import Classes.DatabaseHandlers.addPattern



class AddNotifications(Classes.DatabaseHandlers.addPattern.addPattern):
    def add(self, list):
        Base = declarative_base()

        databaseInstance = SingletonDatabase.Database()
        engine = databaseInstance.engine

        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)

        session = Session()

        sp = list.split('#')
        user = Classes.DatabaseHandlers.create_table.Notifications()
        user.type = sp[1]
        user.notiString = sp[2]
        user.medID = sp[3]
        user.medName = sp[4]
        user.medShelf = sp[5]
        user.status = sp[6]
        session.add(user)
        session.commit()
        session.close()