from Classes.Notifications.MedicineBuildingActivity import MedicineBuildingActivity


class Meds(MedicineBuildingActivity):

    def __init__(self,medID=None,name=None,type=None,company=None,qty=None,price=None,
                 expDate=None,shelf=None,imgLink=None):
        self.medID = medID
        self.name = name
        self.type = type
        self.company = company
        self.qty = qty
        self.price = price
        self.expDate = expDate
        self.shelf = shelf
        self.imgLink = imgLink

    def set_medID(self,medID):
        self.medID=medID
    def set_name(self,name):
        self.name = name
    def set_type(self,type):
        self.type=type
    def set_company(self,company):
        self.company = company
    def set_qty(self,qty):
        self.qty = qty
    def set_price(self,price):
        self.price=price
    def set_ExpDate(self,ExpDate):
        self.expDate = ExpDate
    def set_shelf(self,shelf):
        self.shelf=shelf
    def set_imgLink(self,imgLink):
        self.imgLink = imgLink

