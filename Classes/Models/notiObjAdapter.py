from Classes.Models.HashNotification import HashNotification
from Classes.Models.notification import Notification


class NotiObjAdapter(HashNotification):
    """converts Notification Object inot Hash Format Notification"""

    def __init__(self, notiObj):
        self.notiObj = notiObj

    def getNotificationMsg(self):
        hashed = ""
        hashed += str(self.notiObj.notiID) + "#"
        hashed += self.notiObj.type + "#"
        hashed += self.notiObj.getNotiString() + "#"
        hashed += str(self.notiObj.medID) + "#"
        hashed += self.notiObj.medName + "#"
        hashed += self.notiObj.medShelf + "#"
        hashed += self.notiObj.status
        return hashed;


# new_noti = Notification(notiID=1,
#                                 type="Expired",
#                                 medName="Napa",
#                                 medID=30,
#                                 medShelf="22A",
#                                 status="Unread")
# hashNoti = NotiObjAdapter(new_noti)
# print(hashNoti.getNotificationMsg())
# OUTPUT : 1#Expired#Napa [30, at Shelf: 22A] date expired. Please remove from shelf.#30#Napa#22A#Unread