from Classes.ManageOrders.AbstractOrderMedicine import AbstractOrderMedicine

class DecoratorOrder(AbstractOrderMedicine):
    def __init__(self, decorated_order, medOrders):
        AbstractOrderMedicine.__init__(self,decorated_order)
        self.medOrders = medOrders


    def get_cost(self):
        return self.medOrders.cost + self.decorated_order.get_cost()


