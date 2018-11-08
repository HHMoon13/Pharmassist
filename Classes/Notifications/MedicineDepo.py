from Classes.Notifications.NotificationGenerator import NotificationGenerator
from Classes.Notifications.MedicineCollector import MedicineCollector
from Classes.Notifications.NotificationTableManager import NotificationDatabaseManager

class MedicineDepo(object):
    """Facade pattern to divide works into subclasses"""

    def __init__(self):
        self.medCollector = MedicineCollector()
        self._medicines = self.medCollector.createMedList()

        self.notiGenerator = NotificationGenerator(medicines= self._medicines)
        self._notiObjects = self.notiGenerator.generateNotifications()

        self.notiTable = NotificationDatabaseManager(self.notiGenerator)
        self.notiTable.setNotiObjects(self._notiObjects)
        #self.notiTable.saveNotificationsToDB()


    def getAllMedicine(self):
        return self._medicines

    def getAllNotifications(self):
        return  self._notiObjects

    def saveNotifications(self):
        self.notiTable.saveNotificationsToDB()