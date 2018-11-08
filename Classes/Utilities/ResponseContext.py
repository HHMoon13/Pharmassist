from Classes.Utilities import ResponseState as Response

class ResponseContext:
    def __init__(self, responseState):
        self.responseState = responseState

    def setState(self, newState):
        self.responseState=newState

    def respondToState(self, username, userType):
        self.responseState.respond(username, userType)