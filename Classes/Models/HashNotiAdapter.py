from Classes.Models.notification import Notification


class HashNotiAdapter(Notification):
    """Converts Hash format Notification into Notification Object"""

    def __init__(self, hashNoti):
        self.hashNoti = hashNoti
        parts = self.hashNoti.split("#")
        super().__init__(notiID=parts[0],type=parts[1],medName=parts[4],medID=parts[3],medShelf=parts[5],status=parts[6])


    def getNotiString(self):
        return super().getNotiString()

    def __str__(self):
        return super().__str__()


# hashNoti = '1#Expired#Napa [30, at Shelf: 22A] date expired. Please remove from shelf.#30#Napa#22A#Unread'
# new_noti = HashNotiAdapter(hashNoti)
# print(new_noti.__str__())
# #OUTPUT: {"medID": "30","medName": "Napa", "notiString": "Napa [30, at Shelf: 22A] date expired. Please remove from shelf.", "type": "Expired", "status": "Unread"}
# # new_noti = Notification(notiID=1,
# #                                 type="Expired",
# #                                 medName="Napa",
# #                                 medID=30,
# #                                 medShelf="22A",
# #                                 status="Unread")