from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.create_table as create_table
import Classes.DatabaseHandlers.fetch as fetch
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase
from Classes import Statics

Base = declarative_base()

# engine = sqlalchemy.create_engine('mysql+pymysql://root:1152104@localhost/pharmassistant')
databaseInstance = SingletonDatabase.Database()
engine = databaseInstance.engine

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

userList = []
vendorList = []
medList = []
notificationList = []
orderList = []
sellList = []
expenseList = []
orderlistList = []

def Delete(table, id):
    users = session.query(table).all()
    s = str(table)
    if s == "<class 'Classes.DatabaseHandlers.create_table.Users'>":
        for user in users:
            m = int(user.user_id)
            if m == int(id):
                session.delete(user)
                session.commit()


    elif s == "<class 'Classes.DatabaseHandlers.create_table.Vendors'>":
        for user in users:
            m = int(user.vendor_id)
            if m == int(id):
                session.delete(user)
                session.commit()

    elif s == "<class 'Classes.DatabaseHandlers.create_table.Medicines'>":
        for user in users:
            m = int(user.medicine_id)
            if m == int(id):
                session.delete(user)
                session.commit()

    elif s == "<class 'Classes.DatabaseHandlers.create_table.Notifications'>":
        for user in users:
            m = int(user.notification_id)
            if m == int(id):
                session.delete(user)
                session.commit()

    elif s == "<class 'Classes.DatabaseHandlers.create_table.Orders'>":
        for user in users:
            m = int(user.order_id)
            if m == int(id):
                session.delete(user)
                session.commit()

    elif s == "<class 'Classes.DatabaseHandlers.create_table.OrdersList'>":
        for user in users:
            m = str(user.order_id)
            if m == id:
                session.delete(user)
                session.commit()

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