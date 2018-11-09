from Classes.DatabaseHandlers import addPattern as Factory
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase
import Classes.DatabaseHandlers.create_table
import Classes.DatabaseHandlers.addPattern
import Classes.Statics

Base = declarative_base()

databaseInstance = SingletonDatabase.Database()
engine = databaseInstance.engine

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

class AddOrders(Classes.DatabaseHandlers.addPattern.addPattern):
    def add(self, list):
        sp = list.split('#')
        user = Classes.DatabaseHandlers.create_table.Orders()
        user.order_id = sp[1]
        user.vendor_id = sp[2]
        user.company_name = sp[3]
        user.medicine = sp[4]
        user.quantity = sp[5]
        user.due_date = sp[6]
        user.status = sp[7]
        user.cost = sp[8]
        session.add(user)
        session.commit()