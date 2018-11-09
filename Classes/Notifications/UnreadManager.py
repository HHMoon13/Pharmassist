from Classes.Notifications.Observer import Observer

class UnreadManager():

    class _SingletonUM(Observer):
        def __init__(self):
            pass

    def update(self, newNoti):
        super().update(newNoti)

    def reset(self):
        super().reset()

    ##########################
    instance = None
    def __new__(cls):  # __new__ always a classmethod
        if not UnreadManager.instance:
            UnreadManager.instance = UnreadManager._SingletonMedDEPO()
        return UnreadManager.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
