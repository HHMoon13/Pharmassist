from Classes.DatabaseHandlers import addPattern as Factory
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase
import Classes.DatabaseHandlers.create_table
import Classes.DatabaseHandlers.addPattern

Base = declarative_base()

databaseInstance = SingletonDatabase.Database()
engine = databaseInstance.engine

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

class AddSellings(Classes.DatabaseHandlers.addPattern.addPattern):
    def add(self, list):
        sp = list.split('#')
        user = Classes.DatabaseHandlers.create_table.Sellings()

        user.money = sp[0]
        user.quantity = sp[4]
        user.date = sp[1]
        user.item = sp[2]
        user.customer_name = sp[3]
        session.add(user)
        session.commit()