from abc import ABC, abstractmethod

class Iterator(ABC):
    def __init__(self):
        super(Iterator, self).__init__()

    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def add(self, toAdd):
        pass

    @abstractmethod
    def remove(self, toRemove):
        pass

    @abstractmethod
    def update(self, medName, attribute, newValue):
        pass

    @abstractmethod
    def search(self, toSearch):
        pass

