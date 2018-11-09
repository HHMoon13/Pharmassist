from Classes.Models.notification import Notification


class NotiObjAdapter(Notification):

    def __init__(self, hashNoti):
        self.hashNoti = hashNoti

    def getNotiString(self):
        return super().getNotiString()

    def __str__(self):
        return super().__str__()

