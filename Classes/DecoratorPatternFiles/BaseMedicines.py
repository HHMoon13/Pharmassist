from Classes import Statics
from Classes.DecoratorPatternFiles.Medicines import Medicines



class BaseMedicines(Medicines):



    def __init__(self, medName, quantity):
        self.medName= medName
        self.quantity = quantity
        self.medlist= Statics.medList

    def get_cost(self):
        for i in self.medlist:
            x= i.split("#")
            if x[1] == self.medName:
                unitPrice = x[4]

        return float(unitPrice)*float(self.quantity)





