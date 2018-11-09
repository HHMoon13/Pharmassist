from Classes.Models.HashNotification import HashNotification
from Classes.Models.notification import Notification


class HashNotiAdapter(HashNotification):

    def __init__(self, notiObj):
        self.notificationData = notiObj

    def getNotificationMsg(self):
        hashed = ""
        hashed += str(self.notificationData.notiID) + "#"
        hashed += self.notificationData.type + "#"
        hashed += self.notificationData.getNotiString() + "#"
        hashed += self.notificationData.medID + "#"
        hashed += self.notificationData.medName + "#"
        hashed += self.notificationData.medShelf + "#"
        hashed += self.notificationData.status
        return hashed;

