from Classes.Models.medicine import Medicine
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes.Models.notification import Notification
from Classes.Models.notificationAdapter import NotificationAdapter
from Classes.Utilities import Iterator
import datetime


class MedicineList(object):

    """fetch all the medicines and save to database"""

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

    def generateNotifications(self):
        """generate notifications to save into database"""

        notiStrings = [] #array of strings with delimeter #
        notiID = 0

        for item in self.medicines:
            itemDict= vars(item)
            cnt = float(itemDict['qty'])

            if cnt == 0:
                notification_string = "empty#" + item.__str__()
                new_noti = Notification(notiID,"Empty",notification_string)
                noti_saveToDB = NotificationAdapter(new_noti)
                notiStrings.append(noti_saveToDB.getNotificationMsg())
                notiID+=1

            expDate = itemDict['expDate']
            expDate = datetime.datetime.strptime(expDate, "%Y-%m-%d").date()
            today = datetime.datetime.now().date()

            if today >= expDate:
                notification_string = "expired#" + item.__str__()
                new_noti = Notification(notiID, "Expired", notification_string)
                noti_saveToDB = NotificationAdapter(new_noti)
                notiStrings.append(noti_saveToDB.getNotificationMsg())
                notiID += 1

            #code to save into Databases...

            ###########

        return notiStrings

    def mediList(self):
        list = []
        for item in self.medicines:
            list.append(item.__str__())
        return list


# m = MedicineList()
# m.printList()