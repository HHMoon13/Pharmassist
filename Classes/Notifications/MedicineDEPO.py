
from Classes.Notifications.Subject import Subject
from Classes.Notifications.MedicineCollector import MedicineCollector
from Classes.Notifications import NotiGenerator, NotiTableManager
from Classes.DatabaseHandlers import update,create_table


class MedicineDEPO(Subject):
    """Singleton pattern to ensure single instance\
    Observer Pattern to notify NotificationGenerator and UnreadManager\
    Facade Pattern to divide tasks into different classes"""

    class _SingletonMedDEPO(Subject):
        def __init__(self):
            self._observers = []
            self._newNoti = None
            self.medCollector = MedicineCollector()
            self._medicines = self.medCollector.createMedList()
            self.notiGenerator = NotiGenerator.NotiGenerator()
            self.notiTableMng = NotiTableManager.NotiTableManager()

        def registerObserver(self, observer):
            self._observers.append(observer)

        def removeObserver(self, observer):
            self._observers.remove(observer)

        def notifyAllObserver(self):
            for o in self._observers:
                o.update(self._newNoti)


        def getAllMedicines(self):
            return self._medicines #Medicine Objects

        def addMedicineByID(self,medID,qty):
            pass

        def sellMedicinceByID(self, medID, remQty):
            """Update that medicine's quantity in database
            if it becomes zero, create newEmptyNotification
            notify unreadManager, NotificationTableManager"""

            update.Update(create_table.Medicines, medID, 'quantity', remQty)

            if remQty == 0:
                self._newNoti = self.notiGenerator.generateEmptyNotification(medID=medID, medName="x", medShelf="y",
                                                                             notiID=0)
                self.notifyAllObserver()
                self.notiTableMng.saveSingleNotification(newNotiObj=self._newNoti)
            pass

        def removeMedicineByID(self,medID):
            pass

        def onLoadNotifications(self):
            self.notiGenerator._setMeds(self._medicines)
            firstNotis = self.notiGenerator.firstNotifications()
            self.notiTableMng.saveNotificationList(firstNotis)
            return firstNotis

    ##########################
    instance = None
    def __new__(cls):  # __new__ always a classmethod
        if not MedicineDEPO.instance:
            MedicineDEPO.instance = MedicineDEPO._SingletonMedDEPO()
        return MedicineDEPO.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

