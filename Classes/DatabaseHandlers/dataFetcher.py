from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Classes.DatabaseHandlers.databaseSingleton as SingletonDatabase


def fetchMedicines():
    Base = declarative_base()
    databaseInstance = SingletonDatabase.Database()
    engine = databaseInstance.engine

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    from Classes.DatabaseHandlers import create_table
    meds = session.query(create_table.Medicines).all()

    medList = []
    for med in meds:
        m = str(med.medicine_id)
        s = m + '#' + med.medicine_name + '#' + med.medicine_type + '#' + med.company_name + '#' + str(
            med.price) + '#' + str(med.quantity) + '#' + str(
            med.expiry_date) + '#' + med.shelf + '#' + med.image_link
        medList.append(s)
    #print(medList)
    session.close()
    return medList

def fetchNotifications():
    Base = declarative_base()
    databaseInstance = SingletonDatabase.Database()
    engine = databaseInstance.engine

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    from Classes.DatabaseHandlers import create_table
    result = session.query(create_table.Notifications).all()
    notificationList = []
    for data in result:
        m = str(data.notificationID)
        s = m + '#' + data.type + '#' + data.notiString + '#' + data.medID + '#' + data.medName + '#' + data.medShelf + '#' + data.status
        notificationList.append(s)
        #print(s)
    # print(notificationList)
    session.close()
    return notificationList