from abc import ABC, abstractmethod

class Response(ABC):
    @abstractmethod
    def respond(self, username, userType):
        pass