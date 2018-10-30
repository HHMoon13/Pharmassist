from Classes import Statics
from Classes.Models.medOrders import medOrder


class medOrderList(object) :

    def __init__(self):
        self.medOrders = self.createMedOrderList()


    def createMedOrderList(self):
        orders = []
        orderList = Statics.medorder  # [] #list of objects, will be collected from database

        for item in orderList:
            # print(item)
            sp = str(item).split('#')
            # print(len(sp))
            m = medOrder(sp[0], sp[1], sp[2], sp[3], sp[4], sp[5], sp[6], sp[7], sp[8])
            orders.append(m)
        return orders


    def get_medordersList(self):

        list = []
        for item in self.medOrders:
            list.append(item.__str__())

            #  "\"" +str(item.venID) + "\" : "+         "\"items\" : "

        return list