import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.create_table as create_table
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase
from Classes import Statics
from Classes.DatabaseHandlers import fetch

Base = declarative_base()

databaseInstance = SingletonDatabase.Database()
engine = databaseInstance.engine

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

def Update(table, id, attribute, value):
    s = str(table)
    if s == "<class 'Classes.DatabaseHandlers.create_table.Users'>":
        m = session.query(create_table.Users).filter(create_table.Users.user_id == id).update({attribute: value})
        session.commit()
    elif s == "<class 'Classes.DatabaseHandlers.create_table.Vendors'>":
        m = session.query(create_table.Vendors).filter(create_table.Vendors.vendor_id == id).update({attribute: value})
        session.commit()
    elif s == "<class 'Classes.DatabaseHandlers.create_table.Medicines'>":
        m = session.query(create_table.Medicines).filter(create_table.Medicines.medicine_id == id).update({attribute: value})
        session.commit()
    elif s == "<class 'Classes.DatabaseHandlers.create_table.Orders'>":
        m = session.query(create_table.Orders).filter(create_table.Orders.order_id == id).update({attribute: value})
        session.commit()
    elif s == "<class 'Classes.DatabaseHandlers.create_table.OrdersList'>":
        m = session.query(create_table.OrdersList).filter(create_table.OrdersList.order_id == id).update(
            {attribute: value})
        session.commit()
    elif s == "<class 'Classes.DatabaseHandlers.create_table.Notifications'>":
        m = session.query(create_table.Notifications).filter(create_table.Notifications.notificationID == id).update(
            {attribute: value})
        session.commit()
    #
    # Statics.userList.clear()
    # Statics.vendorList.clear()
    # Statics.medList.clear()
    # Statics.notificationList.clear()
    # Statics.orderList.clear()
    # Statics.sellList.clear()
    # Statics.expenseList.clear()
    # Statics.orderlistList.clear()
    # fetch.Fetch()


#Update(create_table.Medicines, 4, 'medicine_type', 'guuuuuuuu')
session.close()