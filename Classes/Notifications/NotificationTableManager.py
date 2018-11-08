from Classes.DatabaseHandlers.addFactory import addFactory
import Classes.DatabaseHandlers.create_table as create_table
import Classes.DatabaseHandlers.update as notificationUpdater
from Classes.Models.notificationAdapter import NotificationAdapter
from Classes.Notifications.NotificationGenerator import NotificationGenerator
from Classes.Notifications.Observer import Observer


class NotificationDatabaseManager(Observer):
    """save notifications to database and fetch"""

    def __init__(self,notiGenSubject):
        self._subject = NotificationGenerator()
        self._subject = notiGenSubject
        self._subject.registerObserver(self)

        self._hashNotifications = []

    def update(self, newNoti):
        self.saveNewNotiToDB(newNoti)

    def reset(self):
        """update notifications in database from unread to read"""
        print("update notifications in database from unread to read")
        notificationUpdater.update()

    def saveNewNotiToDB(self,newNoti):
        hashNoti = NotificationAdapter(newNoti).getNotificationMsg()
        addFactory.add('', create_table.Notifications, hashNoti)

    def setNotiObjects(self,notiObjects):
        self._notiObjects = notiObjects

    def convertAllToHash(self):
        for notiObj in self._notiObjects:
            notiAdapter = NotificationAdapter(notiObj)
            self._hashNotifications.append(notiAdapter.getNotificationMsg())

    def saveNotificationsToDB(self):
        self.convertAllToHash()
        for hashNoti in self._hashNotifications:
            addFactory.add('',create_table.Notifications, hashNoti)

