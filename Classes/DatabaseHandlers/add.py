from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.create_table as create_table
import Classes.DatabaseHandlers.fetch as fetch
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase


Base = declarative_base()

# engine = sqlalchemy.create_engine('mysql+pymysql://root:1152104@localhost/pharmassistant')
databaseInstance = SingletonDatabase.Database()
engine = databaseInstance.engine

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


def Add(table, list):
    s = str(table)
    sp = list.split('#')
    if s == "<class 'create_table.Users'>":
        user = create_table.Users()
        user.username = sp[1]
        user.full_name = sp[2]
        user.password = sp[3]
        user.user_type = sp[4]
        session.add(user)
        session.commit()

    elif s == "<class 'create_table.Vendors'>":
        user = create_table.Vendors()
        user.company_name = sp[1]
        user.contact_address = sp[2]
        session.add(user)
        session.commit()


    elif s == "<class 'create_table.Medicines'>":
        print(sp)
        user = create_table.Medicines()
        user.medicine_id=sp[0]
        user.company_name = sp[3]
        user.medicine_name = sp[1]
        user.medicine_type = sp[2]
        user.shelf = sp[7]
        user.image_link = sp[8]
        user.quantity = sp[5]
        user.price = sp[4]
        user.expiry_date = sp[6]
        session.add(user)
        session.commit()

    elif s == "<class 'create_table.Orders'>":
        user = create_table.Orders()
        user.vendor_id = sp[1]
        user.company_name = sp[2]
        user.medicine = sp[3]
        user.quantity = sp[4]
        user.due_date = sp[5]
        user.status = sp[6]
        user.cost = sp[7]
        session.add(user)
        session.commit()


    elif s == "<class 'create_table.Notifications'>":
        user = create_table.Notifications()
        user.notification = sp[1]
        user.time = sp[2]
        session.add(user)
        session.commit()


    elif s == "<class 'create_table.Sellings'>":
        user = create_table.Sellings()
        user.money = sp[0]
        user.quantity = sp[4]
        user.date = sp[1]
        user.item = sp[2]
        user.customer_name = sp[3]
        session.add(user)
        session.commit()
       # Money * Date * Item * CashierName * Quantity


    elif s == "<class 'create_table.Expenses'>":
        user = create_table.Expenses()
        user.money = sp[1]
        user.quantity = sp[2]
        user.date = sp[3]
        user.item = sp[4]
        user.vendor = sp[5]
        session.add(user)
        session.commit()


    userList = []
    vendorList = []
    medList = []
    notificationList = []
    orderList = []
    sellList = []
    expenseList = []

    fetch.Fetch()

session.close()