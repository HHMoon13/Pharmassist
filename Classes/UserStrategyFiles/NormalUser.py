from Classes.UserStrategyFiles.MakeAccountBehaviour import CanMakeAccount, CannotMakeAccount
from Classes.UserStrategyFiles.User import User

class NormalUser(User):
    def __init__(self):
        User.MakeAccountBehaviour= CannotMakeAccount()
