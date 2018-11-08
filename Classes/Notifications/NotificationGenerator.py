
from Classes.Notifications.Subject import Subject
from Classes.Models.notification import Notification
import datetime

class NotificationGenerator(Subject):
    """generates notifications after checking all medicines
    uses observer pattern to notify NotificationPageManager about
    new Notifications"""

    _observers = []
    newNotification = None

    def __init__(self,medicines=None):
        self._notifications = [] #will be generated from medlist
        self._allMeds = medicines

    def registerObserver(self,observer):
        NotificationGenerator._observers.append(observer)

    def removeObserver(self, observer):
        NotificationGenerator._observers.remove(observer)

    def notifyAllObserver(self):
        for observer in NotificationGenerator._observers:
            observer.update(NotificationGenerator.newNotification)


    def generateNotifications(self):
        """generate notifications to after checking medicineList"""

        notiID = 0
        for medItem in self._allMeds:
            itemDict= vars(medItem)
            cnt = float(itemDict['qty'])

            if cnt == 0:
                new_noti = NotificationGenerator.generateEmptyNotification(medName=itemDict['name'],
                                                            medID=itemDict['medID'],
                                                            medShelf=itemDict['shelf'],
                                                            notiID=notiID)
                self._notifications.append(new_noti)
                notiID += 1

            expDate = itemDict['expDate']
            expDate = datetime.datetime.strptime(expDate, "%Y-%m-%d").date()
            today = datetime.datetime.now().date()

            if today >= expDate:
                new_noti = NotificationGenerator.generateExpiredNotification(medName=itemDict['name'],
                                        medID=itemDict['medID'],
                                        medShelf=itemDict['shelf'],
                                        notiID=notiID)
                self._notifications.append(new_noti)
                notiID += 1

            print(notiID)
        return self._notifications

    @staticmethod
    def generateEmptyNotification(medID,medName,medShelf,notiID=0):
        new_noti = Notification(notiID=notiID,
                                type="Empty",
                                medName=medName,
                                medID=medID,
                                medShelf=medShelf,
                                status="Unread")
        NotificationGenerator.newNotification = new_noti
        NotificationGenerator.notifyAllObserver(self=None)
        return new_noti

    @staticmethod
    def generateExpiredNotification(medID,medName,medShelf,notiID=0):
        new_noti = Notification(notiID=notiID,
                                type="Expired",
                                medName=medName,
                                medID=medID,
                                medShelf=medShelf,
                                status="Unread")
        NotificationGenerator.newNotification = new_noti
        NotificationGenerator.notifyAllObserver(None)
        return new_noti

    def allRead(self):
        for observer in self._observers:
            observer.reset()


#a = it.Iterator
#a = adn.AccessDatabaseNotifications().DatabaseNotifications
#a.add(oneRowOfData)
# addFactory.add('', create_table.Notifications, addList)
# addList hoilo # er string ta
