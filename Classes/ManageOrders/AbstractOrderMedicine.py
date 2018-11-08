from Classes.ManageOrders.AbstractOrder import AbstractOrder


class AbstractOrderMedicine(AbstractOrder):
    def __init__(self, decorated_order):
        self.decorated_order = decorated_order

    def get_cost(self):
        return self.decorated_order.get_cost()