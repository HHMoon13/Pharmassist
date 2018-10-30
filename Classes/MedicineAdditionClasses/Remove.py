from Classes.Utilities import Operation as op
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes.Utilities import Iterator

class Remove(op.Operation):
    def doOperation(self, msg):
        a = Iterator.Iterator
        a = adm.AccessDatabaseMedicines().getIterator()
        a.remove(msg)