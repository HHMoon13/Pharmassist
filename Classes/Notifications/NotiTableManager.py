from Classes.DatabaseHandlers.addFactory import addFactory as addFactory
import Classes.DatabaseHandlers.create_table as create_table
from Classes.DatabaseHandlers.dataFetcher import fetchNotifications

class NotiTableManager(object):

    def __init__(self):
        pass

    def saveSingleNotification(self,newNotiObj):
        from Classes.Models.notiObjAdapter import NotiObjAdapter
        hashNoti = NotiObjAdapter(newNotiObj).getNotificationMsg()
        #addFactory.add('', create_table.Notifications, hashNoti)
        from Classes.DatabaseHandlers.AddNotifications import AddNotifications
        AddNotifications.add(hashNoti)


    def saveNotificationList(self,notiObjList):
        for notiObj in notiObjList:
            self.saveSingleNotification(notiObj)

    @staticmethod
    def fetchAllNotifications(): # as Notification Object type List
        notiObjList = []
        notiFromDatabase = fetchNotifications()
        for hashNoti in notiFromDatabase:
            from Classes.Models.HashNotiAdapter import HashNotiAdapter
            notiObj = HashNotiAdapter(hashNoti)
            notiObjList.append(notiObj)
        return notiObjList

    @staticmethod
    def fetchUnreadNotifications():
        allNotiObject  = NotiTableManager.fetchAllNotifications()
        unreadList = []
        for noti in allNotiObject:
            if noti.status=="unread":
                unreadList.append(noti)
        return unreadList


    @staticmethod
    def markUnreadToRead():
        import Classes.DatabaseHandlers.updateNotifications as updateNoti
        updateNoti.update()