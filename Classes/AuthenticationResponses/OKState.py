from Classes.Utilities import ResponseState
from Classes import Statics as Statics

class OKState(ResponseState.Response):
    def respond(self, username, userType):
        Statics.authMessage="OK"
        Statics.currentUser=username
        Statics.currentUserType=userType
