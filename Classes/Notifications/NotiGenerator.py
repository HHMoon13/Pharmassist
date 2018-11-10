from Classes.Models.notification import Notification
import datetime


class NotiGenerator(object):

    def __init__(self):
        self._meds = []
        self._notifications = []

    def _setMeds(self,meds):
        self._meds = meds

    @staticmethod
    def generateEmptyNotification(medID, medName, medShelf, notiID=0):
        new_noti = Notification(notiID=notiID,
                                type="Empty",
                                medName=medName,
                                medID=medID,
                                medShelf=medShelf,
                                status="unread")
        from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
        a = adm.AccessDatabaseMedicines().getIterator()
        a.remove(medID)
        return new_noti

    @staticmethod
    def generateExpiredNotification(medID, medName, medShelf, notiID=0):
        new_noti = Notification(notiID=notiID,
                                type="Expired",
                                medName=medName,
                                medID=medID,
                                medShelf=medShelf,
                                status="unread")
        from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
        a = adm.AccessDatabaseMedicines().getIterator()
        a.remove(medID)
        return new_noti

    def fristNotifications(self):
        """generate notifications to after checking medicineList"""

        if(self._meds ==[]):
            print("meds was not set in noti generator")

        notiID = 0
        for medItem in self._meds:
            itemDict= vars(medItem)
            cnt = float(itemDict['qty'])

            if cnt == 0:
                new_noti = NotiGenerator.generateEmptyNotification(medName=itemDict['name'],
                                                            medID=itemDict['medID'],
                                                            medShelf=itemDict['shelf'],
                                                            notiID=notiID)
                self._notifications.append(new_noti)
                #delete this medicine too.

                notiID += 1

            expDate = itemDict['expDate']
            expDate = datetime.datetime.strptime(expDate, "%Y-%m-%d").date()
            today = datetime.datetime.now().date()

            if today >= expDate:
                new_noti = NotiGenerator.generateExpiredNotification(medName=itemDict['name'],
                                        medID=itemDict['medID'],
                                        medShelf=itemDict['shelf'],
                                        notiID=notiID)
                self._notifications.append(new_noti)
                notiID += 1

            print(notiID)
        return self._notifications