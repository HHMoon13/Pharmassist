class User(object):

    def __init__(self):
        self.MakeAccountBehaviour=None

    def TryingToMakeAccount(self):
        return self.MakeAccountBehaviour.tryToAddAccount()