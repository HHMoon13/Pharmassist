from Classes.ManageOrders.AbstractOrder import AbstractOrder


class BaseOrder(AbstractOrder):
    def __init__(self, newOrder):
        self.newOrder = newOrder

    def get_cost(self):
        return self.newOrder.totalCost


