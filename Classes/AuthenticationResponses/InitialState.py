from Classes.Utilities import ResponseState
from Classes import Statics as Statics

class InitialState(ResponseState.Response):
    def respond(self, username, userType):
        Statics.currentUser = "NOUSER"
        Statics.currentUserType = "NONE"
        Statics.authMessage = "None"
