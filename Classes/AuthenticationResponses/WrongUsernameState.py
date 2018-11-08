from Classes.Utilities import ResponseState
from Classes import Statics as Statics


class WrongUsernameState(ResponseState.Response):
    def respond(self, username, userType):
        Statics.authMessage = "Wrong Username"
        Statics.currentUser = username
        Statics.currentUserType = userType
