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



class AddMedicines(Classes.DatabaseHandlers.addPattern.addPattern):
    def add(self, list):
        sp = list.split('#')
        user = Classes.DatabaseHandlers.create_table.Medicines()
        user.medicine_id = sp[0]
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