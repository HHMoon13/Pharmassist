from Classes.Utilities import ResponseState
from Classes import Statics as Statics


class WrongPasswordState(ResponseState.Response):
    def respond(self, username, userType):
        Statics.authMessage = "Wrong Password"
