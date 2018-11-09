from Classes.DecoratorPatternFiles.Medicines import Medicines


class AbstractMedicineDecorator(Medicines):

    def __init__(self, decorated_medicine):
        self.decorated_medicine = decorated_medicine

    def get_cost(self):
        return self.decorated_medicine.get_cost()

