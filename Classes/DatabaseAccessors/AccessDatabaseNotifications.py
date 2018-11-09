from abc import ABC, abstractmethod

from Classes.DatabaseHandlers import create_table as create_table
from Classes.DatabaseHandlers import add, delete, create_table, update, addFactory
from Classes.Utilities import Iterator, Container
from Classes import Statics

class AccessDatabaseNotifications(Container.Container):

    def __init__(self):
        super(Container.Container, self).__init__()


    def getIterator(self):
        return AccessDatabaseNotifications.DatabaseNotifications()



    class DatabaseNotifications(Iterator.Iterator):
        def __init__(self, index=0):
            self.index=0

        def hasNext(self):
            if self.index < Statics.notificationList.__len__():
                return True
            else:
                return False

        def next(self):
            if self.hasNext():
                a = Statics.notificationList.__getitem__(self.index)
                self.index += 1
                return a
            else:
                self.index=0

        def add(self, toAdd):
            temp=toAdd
            addFactory.addFactory().add(create_table.Notifications, str(toAdd))

        def remove(self, toBeRemove):
            temp=toBeRemove
            delete.Delete(create_table.Notifications, toBeRemove)
            #pass temp to a database management class method

        def update(self, medID, attribute, newValue):
            update.Update("<class 'Classes.DatabaseHandlers.create_table.Medicines'>", medID, attribute, newValue)
            #dowork

        def search(self, toSearch):
            temp=""
            #pass temp to a database management class method which returns the search result
            return temp