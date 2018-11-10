from abc import ABC, abstractmethod
from Classes.Utilities import Iterator, Container
from Classes import Statics
from Classes.DatabaseHandlers import addFactory, delete, create_table

class AccessDatabaseExpenses(Container.Container):

    def __init__(self):
        super(Container.Container, self).__init__()


    def getIterator(self):
        return AccessDatabaseExpenses.DatabaseExpenses()



    class DatabaseExpenses(Iterator.Iterator):
        def __init__(self, index=0):
            self.index=0

        def hasNext(self):
            if self.index < Statics.expenseList.__len__():
                return True
            else:
                return False

        def next(self):
            if self.hasNext():
                a = Statics.expenseList.__getitem__(self.index)
                self.index += 1
                return a
            else:
                self.index=0

        def add(self, toAdd):
            addFactory.addFactory().add(create_table.Expenses, str(toAdd))

        def remove(self, toBeRemove):
            delete.Delete(create_table.Expenses, int(toBeRemove))

        def update(self, medName, attribute, newValue):
            pass

        def search(self, toSearch):
            pass
