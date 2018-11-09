from Classes.Utilities import Operation as op
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes.Utilities import Iterator

class NoOperation(op.Operation):
    def doOperation(self, msg):
        print("No available operations.")
