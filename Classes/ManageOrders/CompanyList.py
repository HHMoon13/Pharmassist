#from Classes.Notifications.Observable import Observable
from Classes.Models.vendors import Vendor
import json
import datetime


class CompanyList(object):

    """all the medicines"""

    def __init__(self):
        self.vendors = self.createVendorsList()

    def createVendorsList(self):

        vendors = [] #list of objects, will be collected from database
        v1 = Vendor("v001", "Square", "01XXXXXXXX")
        v2 = Vendor("v002", "Beximco Pharma Limited", "01XXXXXXXX")
        v3 = Vendor("v003", "Incepta Pharma Limited", "01XXXXXXXX")
        v4 = Vendor("v004", "Aristopharma Limited", "01XXXXXXXX")

        vendors.append(v1)
        vendors.append(v2)
        vendors.append(v3)
        vendors.append(v4)

        return vendors

    def vendorsList(self):
        list = []
        for item in self.vendors:
            list.append(item.__str__())

            #  "\"" +str(item.venID) + "\" : "+         "\"items\" : "

        return list

    def printList(self):

        for item in self.vendors:
            itemDict = vars(item)
            print(itemDict['venID']+" : "+itemDict['name'] +" : "+itemDict['contact'])




