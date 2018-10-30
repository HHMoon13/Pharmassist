from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.create_table as create_table
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase


Base = declarative_base()

# engine = sqlalchemy.create_engine('mysql+pymysql://root:1152104@localhost/pharmassistant')
databaseInstance = SingletonDatabase.Database()
engine = databaseInstance.engine

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

userList = [None]*100
vendorList = [None]*100
medList = [None]*100
notificationList = [None]*100
orderList = [None]*100
sellList = [None]*100
expenseList = [None]*100


def Delete(table, id):
    users = session.query(table).all()
    s = str(table)
    if s == "<class 'create_table.Users'>":
        for user in users:
            m = int(user.user_id)
            if m == id:
                session.delete(user)
                session.commit()


    elif s == "<class 'create_table.Vendors'>":
        for user in users:
            m = int(user.vendor_id)
            if m == id:
                session.delete(user)
                session.commit()

    elif s == "<class 'create_table.Medicines'>":
        for user in users:
            m = int(user.medicine_id)
            if m == id:
                session.delete(user)
                session.commit()

    elif s == "<class 'create_table.Notifications'>":
        for user in users:
            m = int(user.notification_id)
            if m == id:
                session.delete(user)
                session.commit()

    elif s == "<class 'create_table.Orders'>":
        for user in users:
            m = int(user.order_id)
            if m == id:
                session.delete(user)
                session.commit()




Delete(create_table.Medicines, 4)
session.close()