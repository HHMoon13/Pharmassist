from Classes.Utilities import Iterator, Container
from Classes import Statics
from Classes.DatabaseHandlers import add, delete, create_table, update, addFactory

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
            addFactory.addFactory().add(create_table.Medicines, str(toAdd))

        def remove(self, toBeRemove):
            delete.Delete(create_table.Medicines, str(toBeRemove))

        def update(self, medID, attribute, newValue):
            print(medID, attribute, newValue)
            update.Update("<class 'Classes.DatabaseHandlers.create_table.Medicines'>", medID, attribute, newValue)
            pass
            #dowork

        def search(self, toSearch):
            result=[]
            if toSearch=="":
                result = "No Matches"
                return result
            while self.hasNext():
                temp1 = self.next()
                temp2 = temp1.split("#")
                for i in temp2:
                    if (i.capitalize()).__contains__((Statics.searchKey).capitalize()):
                        result.append(temp1)
                        break
            if result.__len__()==0:
                result = "No Matches"
            return result
