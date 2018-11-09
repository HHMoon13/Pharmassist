#from Classes.Notifications.Observable import Observable
from Classes import Statics
from Classes.Models.vendors import Vendor
import json
import datetime


class CompanyList(object):

    """all the medicines"""

    def __init__(self):
        self.vendors = self.createVendorsList()

    def createVendorsList(self):


        vendors = []
        vendorsList = Statics.vendorList  # [] #list of objects, will be collected from database

        for item in vendorsList:
            #print(item)

            sp = str(item).split('#')
            print(len(sp))
            m = Vendor(sp[0], sp[1], sp[2])
            vendors.append(m)

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




