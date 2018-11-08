
from Classes.Notifications.Observer import Observer
from Classes.Notifications.NotificationGenerator import NotificationGenerator

class UnreadNotificationManager(Observer):
    """uses observer pattern to get notifications from NotificationGenerator"""

    unreadCount  = 0
    unreadNotis = []

    def __init__(self,notiGenSubject):
        self._subject = NotificationGenerator()
        self._subject = notiGenSubject
        self._subject.registerObserver(self)

    def update(self, newNoti):
        UnreadNotificationManager.unreadCount +=1
        UnreadNotificationManager.unreadNotis.append(newNoti)

    def reset(self):
        UnreadNotificationManager.unreadCount = 0
        UnreadNotificationManager.unreadNotis = []

    def getUnreadNotifications(self):
        i = 0;
        u = []
        for unread in UnreadNotificationManager.unreadNotis:
            u.append(unread._str__())
            i += 1;
            if (i > 3):
                break
        return u