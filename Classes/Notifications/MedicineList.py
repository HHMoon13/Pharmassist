#from Classes.Notifications.Observable import Observable
from Classes.Models.medicine import Medicine
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes.Utilities import Iterator
import datetime


class MedicineList(object):

    """all the medicines"""

    def __init__(self):
        self.medicines = self.createMedList()

    def createMedList(self):

        # medFromDatabase = [ "Saline01#Orsaline#Saline#1#50#01-07-2019#11A#/static/Images/orsaline.jpg",
        #                       "Util01#Bandages#Utilities#2#50#01-01-2020#12B#/static/Images/bandages.jpg"]
        medFromDatabase = []
        a = adm.AccessDatabaseMedicines().getIterator()
        while a.hasNext():
            medFromDatabase.append(a.next())

        m = []
        for med in medFromDatabase:
            medAttrs = med.split("#")
            # __init__(self,medID,name,type,qty,price,expDate,shelf,imgLink):
            medicine = Medicine(medAttrs[0],medAttrs[1],medAttrs[2],medAttrs[3],
                                medAttrs[5],medAttrs[4],medAttrs[6],medAttrs[7],medAttrs[8])
            m.append(medicine)

        #extra medicines for testing


        medicines = []
        for mi in m:
            medicines.append(mi)

        return medicines

    def printList(self):

        for item in self.medicines:
            itemDict = vars(item)
            print(itemDict['medID']+" : "+itemDict['qty'] +" : "+itemDict['expDate'])

    def sendNotifications(self):

        notifications = [] #array of strings

        for item in self.medicines:
            itemDict= vars(item)
            cnt = float(itemDict['qty'])

            if cnt == 0:
                notification_string = "empty#"+ item.__str__()
                notifications.append(notification_string)
                #print(item.__str__())

            expDate = itemDict['expDate']
            expDate = datetime.datetime.strptime(expDate, "%Y-%m-%d").date()
            today = datetime.datetime.now().date()
            if today >= expDate:
                notification_string = "expired#" + item.__str__()
                notifications.append(notification_string)

        return notifications

    def mediList(self):
        list = []
        for item in self.medicines:
            list.append(item.__str__())
        return list

m = MedicineList()
for item in m.medicines:
    print(item.__str__())
# print(m.sendCountNotifications())
# print("Expired: ")
# print(m.sendExpiryNotifications())


