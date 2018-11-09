from abc import ABC, abstractmethod
import Classes
from Classes.Utilities import Iterator, Container
from Classes import Statics
from Classes.DatabaseHandlers import  delete, update
from  Classes.DatabaseHandlers import create_table as create_table

class AccessDatabaseOrdersList(Container.Container):

    def __init__(self):
        super(Container.Container, self).__init__()


    def getIterator(self):
        return AccessDatabaseOrdersList.DatabaseOrders()



    class DatabaseOrders(Iterator.Iterator):
        def __init__(self, index=0):
            self.index=0

        def hasNext(self):
            if self.index < Statics.orderList.__len__():
                return True
            else:
                return False

        def next(self):
            if self.hasNext():
                a = Statics.orderList.__getitem__(self.index)
                self.index += 1
                return a
            else:
                self.index=0

        def add(self, toAdd):
            temp=toAdd

            #pass temp to a database management class method

        def remove(self, toBeRemove):
            temp=toBeRemove
            delete.Delete(create_table.OrdersList, toBeRemove)
            #pass temp to a database management class method

        def update(self, medName, attribute, newValue):
            temp=medName
            update.Update(create_table.OrdersList, int(medName), attribute, newValue)

            #dowork

        def search(self, toSearch):
            temp=""
            #pass temp to a database management class method which returns the search result
            return temp
