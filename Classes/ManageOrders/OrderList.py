#from Classes.Notifications.Observable import Observable
from Classes import Statics
from Classes.ManageOrders import medOrderList
from Classes.Models.orders import Order
import json
import datetime


class OrderList(object):

    def __init__(self):
        self.order = self.createOrdersList()

    def createOrdersList(self):

        orders = []
        orderList = Statics.orderlistList  # [] #list of objects, will be collected from database

        for item in orderList:
            # print(item)
            sp = str(item).split('#')
            # print(len(sp))
            m = Order(sp[0], sp[1], sp[2], sp[3], sp[4], sp[5], sp[6], sp[7])
            orders.append(m)
        return orders

    def get_ordersList(self):
        list = []
        for item in self.order:
            list.append(item.__str__())

            #  "\"" +str(item.venID) + "\" : "+         "\"items\" : "

        return list

    def mapOrder(self):
        mediOrder = medOrderList.medOrderList()
        medilist = mediOrder.get_medordersList()
        orders = []
        for item in self.order:
            list = []
            for med in medilist:

                medi = json.loads(med)
                if medi["order_id"] == item.orderID:
                    list.append(medi)

            str = item.orderID + " : " + list
            orders.append(str)

        print(orders)



    def addOrder(self,order):
        m = Order("003", order['companyName'], sp[2], sp[3], sp[4], sp[5], sp[6], sp[7])

    def get_cost(self):
        pass