from abc import ABC, abstractmethod


class MakeAccountBehaviour(object):
    @abstractmethod
    def tryToAddAccount(self):
        pass


class CanMakeAccount(MakeAccountBehaviour):

    def tryToAddAccount(self):
        return True


class CannotMakeAccount(MakeAccountBehaviour):
    def tryToAddAccount(self):
        return False