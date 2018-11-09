from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def doOperation(self, msg):
        pass