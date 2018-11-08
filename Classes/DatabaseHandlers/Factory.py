from Classes.DatabaseHandlers.AddExpenses import AddExpenses
from Classes.DatabaseHandlers.AddMedicines import AddMedicines
from Classes.DatabaseHandlers.AddNotifications import AddNotifications
from Classes.DatabaseHandlers.AddOrders import AddOrders
from Classes.DatabaseHandlers.AddSellings import AddSellings
from Classes.DatabaseHandlers.AddUsers import *
from Classes.DatabaseHandlers.AddVendors import AddVendors


class Factory:
    def getClass(self, string):
        if string == "<class 'Classes.DatabaseHandlers.create_table.Users'>":
            return AddUsers()
        elif string == "<class 'Classes.DatabaseHandlers.create_table.Vendors'>":
            return AddVendors()
        elif string == "<class 'Classes.DatabaseHandlers.create_table.Medicines'>":
            return AddMedicines()
        elif string == "<class 'Classes.DatabaseHandlers.create_table.Orders'>":
            return AddOrders()
        elif string == "<class 'Classes.DatabaseHandlers.create_table.Notifications'>":
            return AddNotifications()
        elif string == "<class 'Classes.DatabaseHandlers.create_table.Sellings'>":
            return AddSellings()
        elif string == "<class 'Classes.DatabaseHandlers.create_table.Expenses'>":
            return AddExpenses()


