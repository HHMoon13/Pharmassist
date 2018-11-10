
class Subject(object):
    """abstract subject class of observer pattern"""

    def registerObserver(self,observer):
        pass

    def removeObserver(self, observer):
        pass

    def notifyAllObserver(self):
        pass
