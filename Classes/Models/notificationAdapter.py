from Classes.Models.hashedNotification import HashFormatNotification
from Classes.Models.notification import Notification


class NotificationAdapter(HashFormatNotification):

    def __init__(self, notificationData):
        self.notificationData = notificationData

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

