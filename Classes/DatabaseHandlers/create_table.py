from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Numeric, Date, Time, Boolean
from sqlalchemy.ext.declarative import declarative_base
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    user_id = Column('id', Integer, primary_key=True)
    username = Column('username', String(50), unique=True)
    password = Column('password', String(50))
    full_name = Column('full_name', String(50))
    user_type = Column('user_type', String(50))


class Vendors(Base):
    __tablename__ = "vendors"

    vendor_id = Column('vendor_id', Integer, primary_key=True)
    company_name = Column('company_name', String(50), unique=True)
    contact_number = Column('contact_number', String(50))


class Medicines(Base):
    __tablename__ = "medicines"

    medicine_id = Column('medicine_id', Integer, primary_key=True)
    medicine_name = Column('medicine_name', String(50))
    medicine_type = Column('medicine_type', String(50))
    company_name = Column('company_name', String(50))
    price = Column('price', Float)
    quantity = Column('quantity', Numeric(50))
    expiry_date = Column('expiry_date', Date)
    shelf = Column('shelf', String(50))
    image_link = Column('image_link', String(50))

class OrdersList(Base):
    __tablename__ = "ordersList"

    order_id = Column('order_id', Integer, primary_key=True)
    company_name = Column('company_name', String(50))
    total_cost = Column('total_cost', Float)
    paid_amount = Column('paid_amount', Float)
    due_amount = Column('due_amount', Float)
    status = Column('status', String(50))
    order_date = Column('order_date', Date)
    due_date = Column('due_date', Date)

class Orders(Base):
        __tablename__ = "orders"

        id = Column('id', Integer, primary_key=True)
        order_id = Column('order_id', String(50))
        vendor_id = Column('vendor_id', Integer)
        company_name = Column('company_name', String(50))
        medicine = Column('medicine', String(50))
        quantity = Column('quantity', Numeric(50))
        due_date = Column('due_date', Date)
        status = Column('status', String(50))
        cost = Column('cost', Numeric(50))


class Notifications(Base):
    __tablename__ = "notifications"

    notificationID = Column('notificationID', Integer, primary_key=True)
    type = Column('type', String(50))
    notiString = Column('notiString', String(50))
    medID = Column('medID', String(50))
    medName = Column('medName', String(50))
    medShelf = Column('medShelf', String(50))
    status = Column('status', String(50))


class Sellings(Base):
        __tablename__ = "sellings"

        sellings_id = Column('sellings_id', Integer, primary_key=True)
        money = Column('money', Numeric(50))
        quantity = Column('quantity', Numeric(50))
        date = Column('date', Date)
        item = Column('item', String(50))
        customer_name = Column('customer_name', String(50))


class Expenses(Base):
            __tablename__ = "expenses"

            expenses_id = Column('expenses_id', Integer, primary_key=True)
            money = Column('money', Numeric(50))
            quantity = Column('quantity', Numeric(50))
            date = Column('date', Date)
            item = Column('item', String(50))
            vendor = Column('vendor', String(50))


# engine = sqlalchemy.create_engine('mysql+pymysql://root:1152104@localhost/pharmassistant')

databaseInstance = SingletonDatabase.Database()
engine = databaseInstance.engine
Base.metadata.create_all(bind=engine)