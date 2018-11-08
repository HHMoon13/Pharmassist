from flask import *
from Classes.Notifications.NotificationGenerator import NotificationGenerator
from Classes.Notifications.MedicineDepo import MedicineDepo

class NotificationPageManager():

    def __init__(self):
        self._medDepo = MedicineDepo()

    def showAllNotifications(self):
        JSONableNotifications = []
        notiObjects = self._medDepo.getAllNotifications()
        for noti in notiObjects:
            JSONableNotifications.append(noti.__str__())

        for j in JSONableNotifications:
            print(j)

        self._medDepo.notiGenerator.allRead()
        return render_template('notificationPage.html', notifications=JSONableNotifications)





