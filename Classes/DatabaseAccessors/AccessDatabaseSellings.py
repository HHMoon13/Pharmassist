from abc import ABC, abstractmethod
from Classes.Utilities import Iterator, Container
from Classes import Statics
from Classes.DatabaseHandlers import addFactory, create_table
from Classes.DatabaseHandlers import update


class AccessDatabaseSellings(Container.Container):

    def __init__(self):
        super(Container.Container, self).__init__()


    def getIterator(self):
        return AccessDatabaseSellings.DatabaseSellings()



    class DatabaseSellings(Iterator.Iterator):
        def __init__(self, index=0):
            self.index=0

        def hasNext(self):
            if self.index < Statics.sellList.__len__():
                return True
            else:
                return False

        def next(self):
            if self.hasNext():
                a = Statics.sellList.__getitem__(self.index)
                self.index += 1
                return a
            else:
                self.index=0

        def add(self, toAdd):
            temp=toAdd
            #pass temp to a database management class method
            addFactory.addFactory().add(create_table.Sellings, toAdd)

        def remove(self, toBeRemove):
            temp=toBeRemove
            #pass temp to a database management class method

        def update(self, id, attribute, newValue):
            temp=id
            update.update(create_table.Sellings, id, attribute, newValue)
            #dowork

        def search(self, toSearch):
            temp=""
            #pass temp to a database management class method which returns the search result
            return temp
