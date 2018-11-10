import Classes
from Classes import Statics

from Classes.ManageOrders.BaseOrder import BaseOrder
from Classes.ManageOrders.DecoratorOrder import DecoratorOrder
from Classes.Models.medOrders import medOrder
from Classes.Models.orders import Order
from Classes.DatabaseHandlers import addFactory
from Classes.DatabaseHandlers import create_table as create_table
from Classes.Utilities import Iterator
from Classes.DatabaseAccessors import AccessDatabaseOrdersList
import json

class makeOrder(object):
    orders = Order(1," ",0,0,0,"false",0,0)
    mediOrderList = []
    totalCost = 0
    base = BaseOrder(orders)
    decorator = base

    @staticmethod
    def setCompanyName(companyName):
        makeOrder.orders = Order(1,companyName,0,0,0,"false",0,0)
        makeOrder.mediOrderList = []
        makeOrder.totalCost = 0
        makeOrder.base = BaseOrder(makeOrder.orders)
        makeOrder.decorator = makeOrder.base


    @staticmethod
    def setTotalCost(cost):
        makeOrder.orders.totalCost = cost

    @staticmethod
    def addItem(data):
        m = medOrder(data['orderID'], data['order_id'], data['venID'], data['companyName'], data['medName'],data['qty'], data['dueDate'], data['status'], data['cost'])
        #print(m)

        makeOrder.decorator = DecoratorOrder(makeOrder.decorator,m)
        makeOrder.mediOrderList.append(m)
        result = makeOrder.decorator.get_cost()

        makeOrder.totalCost = result
        makeOrder.setTotalCost(result)
        return result

    @staticmethod
    def get_order(self):
        return self.orders

    @staticmethod
    def generateOrder(orderData):
        #self,orderID,companyName,totalCost,paid,due,status,orderDate,dueDate)
        order = ""
        makeOrder.orders.totalCost = str(makeOrder.totalCost)
        makeOrder.orders.orderID = "0"
        paid = float(orderData['paid'])
        if paid > makeOrder.totalCost:
            paid = makeOrder.totalCost
        makeOrder.orders.paid = str(paid)
        makeOrder.orders.due = str(float(makeOrder.totalCost) - paid)
        makeOrder.orders.status = "false"
        makeOrder.orders.orderDate = str(orderData['orderDate'])
        makeOrder.orders.dueDate = str(orderData['dueDate'])
        data = makeOrder.orders.stringData()
        print(data)
        a = Classes.DatabaseHandlers.addFactory
        a.addFactory.add('', create_table.OrdersList, str(data))
        makeOrder.saveOrders()
        #Classes.DatabaseHandlers.addFactory.add.add('', create_table.OrdersList, data)

    @staticmethod
    def objectToString(obj):
        data = "003"
        obj = json.load(obj)
        for i in obj:
            if i != "orderID":
                data += "#" + obj[i]

        print(data)

    @staticmethod
    def saveOrders():
        newOrder = makeOrder.mediOrderList
        for item in newOrder:
            item.order_id = Statics.munia_order_id

            print(item.stringData())
            data = item.stringData()
            a = Classes.DatabaseHandlers.addFactory
            a.addFactory.add('', create_table.Orders, str(data))


    @staticmethod
    def updateOrder(orderData):
        makeOrder.orders.totalCost = str(orderData['totalCost'])
        due = float(orderData['due'])
        paid = float(orderData['paid'])
        print(paid)
        if due == 0:
            paid = float(makeOrder.orders.totalCost)
        else:
            paid = float(makeOrder.orders.totalCost) - float(due)
        print(paid)
        makeOrder.orders.paid = str(paid)
        makeOrder.orders.due = str(due)
        print(makeOrder.orders.due)
        makeOrder.orders.orderID = orderData['orderID']

        makeOrder.orders.orderDate = str(orderData['orderDate'])
        makeOrder.orders.dueDate = str(orderData['dueDate'])
        orderID = makeOrder.orders.orderID
        makeOrder.orders.companyName = str(orderData['companyName'])


        a = Iterator.Iterator
        a = AccessDatabaseOrdersList.AccessDatabaseOrdersList().getIterator()
        a.update(orderID, 'due_amount', str(makeOrder.orders.due))
        a.update(orderID,'paid_amount',str(makeOrder.orders.paid))

        a.update(orderID,'status',orderData['status'])

