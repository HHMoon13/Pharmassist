from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.create_table as create_table
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase
import Classes.DatabaseHandlers.Factory


Base = declarative_base()

# engine = sqlalchemy.create_engine('mysql+pymysql://root:1152104@localhost/pharmassistant')
databaseInstance = SingletonDatabase.Database()
engine = databaseInstance.engine

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


class addFactory:

    def add(self, table, list):

        s = str(table)

        a = Classes.DatabaseHandlers.Factory
        b = a.Factory.getClass('', s)
        b.add(list)


#addList = '5#1#3#Mono#guuu#15#2011-11-01#True#200'
#addFactory.add('', create_table.Orders, addList)
session.close()