from Classes.Utilities import Operation as op
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes.Utilities import Iterator

class Update(op.Operation):
    def doOperation(self, msg):
        a = Iterator.Iterator
        a = adm.AccessDatabaseMedicines().getIterator()
        toSend = msg.split("#")
        print(toSend)
        a.update(int(toSend[0]), toSend[1], toSend[2])