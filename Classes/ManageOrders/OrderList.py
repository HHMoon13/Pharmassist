#from Classes.Notifications.Observable import Observable
from Classes import Statics
from Classes.Models.orders import Order
import json
import datetime


class OrderList(object):

    """all the medicines"""

    def __init__(self):
        self.order = self.createOrdersList()

    def createOrdersList(self):

        orders = []
        orderList = Statics.orderList  # [] #list of objects, will be collected from database

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





