from Classes.Utilities import Operation as op
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes.Utilities import Iterator

class Add(op.Operation):
    def doOperation(self, msg):
        a = Iterator.Iterator
        a = adm.AccessDatabaseMedicines().getIterator()
        a.add(msg)
