from Classes.Notifications.Observer import Observer

class UnreadManager():

    class _SingletonUM(Observer):
        def __init__(self, subject):
            self.subject = subject
            self.subject.registerObserver(self)

            from Classes.Notifications.NotiTableManager import NotiTableManager
            n = NotiTableManager()
            unreadList = n.fetchUnreadNotifications()
            showables = []
            for noti in unreadList:
                showables.append(noti.getShortString())

            self.unreadCounter = len(showables)
            self.unreadList = showables

            pass

        def update(self,newNoti):
            self.unreadList.append(newNoti.getShortString())
            self.unreadCounter +=1

        def reset(self):
            self.unreadCounter =0
            self.unreadList = []

        def getUnreadCount(self):
            return  self.unreadCounter
        def getUnreadList(self):
            return self.unreadList


    ##########################
    instance = None
    def __new__(cls,subject):  # __new__ always a classmethod
        if not UnreadManager.instance:
            UnreadManager.instance = UnreadManager._SingletonUM(subject)
        return UnreadManager.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
