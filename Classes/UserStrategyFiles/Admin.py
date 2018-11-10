from Classes.UserStrategyFiles.MakeAccountBehaviour import CanMakeAccount, CannotMakeAccount
from Classes.UserStrategyFiles.User import User

class Admin(User):
    def __init__(self):
        User.MakeAccountBehaviour= CanMakeAccount()