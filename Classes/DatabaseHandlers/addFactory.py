from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.create_table as create_table
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase
import Classes.DatabaseHandlers.Factory
from Classes import Statics
from Classes.DatabaseHandlers import fetch


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
        #print(list)
        Statics.userList.clear()
        Statics.vendorList.clear()
        Statics.medList.clear()
        Statics.notificationList.clear()
        Statics.orderList.clear()
        Statics.sellList.clear()
        Statics.expenseList.clear()
        Statics.orderlistList.clear()
        fetch.Fetch()

session.close()