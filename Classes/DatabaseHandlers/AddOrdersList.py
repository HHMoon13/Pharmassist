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

class AddOrdersList(Classes.DatabaseHandlers.addPattern.addPattern):
    def add(self, list):
        sp = list.split('#')
        user = Classes.DatabaseHandlers.create_table.OrdersList()
        if sp[0] == '0':
            user.company_name = sp[1]
            user.total_cost = sp[2]
            user.paid_amount = sp[3]
            user.due_amount = sp[4]
            user.status = sp[5]
            user.order_date = sp[6]
            user.due_date = sp[7]
            session.add(user)
            session.commit()
        else:
            user.order_id = sp[0]
            user.company_name = sp[1]
            user.total_cost = sp[2]
            user.paid_amount = sp[3]
            user.due_amount = sp[4]
            user.status = sp[5]
            user.order_date = sp[6]
            user.due_date = sp[7]
            session.add(user)
            session.commit()

        prev_i = 1
        users = session.query(Classes.DatabaseHandlers.create_table.OrdersList).all()
        for i in users:
            needed_id = max(i.order_id, prev_i)
            prev_i = i.order_id

        Classes.Statics.munia_order_id = str(needed_id)
        print("k")
        print(Classes.Statics.munia_order_id)