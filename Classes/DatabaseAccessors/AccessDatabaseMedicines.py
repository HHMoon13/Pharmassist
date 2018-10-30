from abc import ABC, abstractmethod
from Classes.Utilities import Iterator, Container
from Classes import Statics

class AccessDatabaseMedicines(Container.Container):

    def __init__(self):
        super(Container.Container, self).__init__()


    def getIterator(self):
        return AccessDatabaseMedicines.DatabaseMedicines()



    class DatabaseMedicines(Iterator.Iterator):
        def __init__(self, index=0):
            self.index=0

        def hasNext(self):
            if self.index < Statics.medList.__len__():
                return True
            else:
                return False

        def next(self):
            if self.hasNext():
                a = Statics.medList.__getitem__(self.index)
                self.index += 1
                return a
            else:
                self.index=0

        def add(self, toAdd):
            temp=toAdd
            #pass temp to a database management class method

        def remove(self, toBeRemove):
            temp=toBeRemove
            #pass temp to a database management class method

        def update(self, medName, attribute, newValue):
            temp=medName
            #dowork

        def search(self, toSearch):
            result=""
            while self.hasNext():
                temp1 = self.next()
                temp2 = temp1.split("#")
                for i in temp2:
                    if (i.capitalize()).__contains__((Statics.searchKey).capitalize()):
                        result += temp1 + "*"
                        break
            if result == "" or toSearch=="":
                result = "No Matches"
            return result
