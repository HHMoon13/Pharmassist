from abc import ABC, abstractmethod

class Container(ABC):
    def __init__(self):
        super(Container, self).__init__()

    @abstractmethod
    def getIterator(self):
        pass