from Classes import Statics
from Classes.DecoratorPatternFiles.AbstractMedicineDecorator import AbstractMedicineDecorator


class DecoratorMedicine(AbstractMedicineDecorator):

    def __init__(self, decorated_medicine,medName,quantity):
        AbstractMedicineDecorator.__init__(self, decorated_medicine)
        self.medName = medName
        self.quantity = quantity
        self.medlist = Statics.medList

    def get_cost(self):
        for i in self.medlist:
            x= i.split("#")
            if x[1] == self.medName:
                unitPrice = x[3]
                break

        return float(unitPrice)*float(self.quantity) + self.decorated_medicine.get_cost()




