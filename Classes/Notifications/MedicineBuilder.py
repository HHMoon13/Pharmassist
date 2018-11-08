class MedicineBuilder(object):
    def __init__(self, Meds):
        self.Meds = Meds

    def build_medID(self,medID):
        self.Meds.set_medID(medID)
    def build_name(self,name):
        self.Meds.set_name(name)
    def build_type(self,type):
        self.Meds.set_type(type)
    def build_company(self,company):
        self.Meds.set_company()
    def build_qty(self,qty):
        self.Meds.set_qty(qty)
    def build_price(self,price):
        self.Meds.set_price(price)
    def build_ExpDate(self,ExpDate):
        self.Meds.set_ExpDate(ExpDate)
    def build_shelf(self,shelf):
        self.Meds.set_shelf(shelf)
    def build_imgLink(self,imgLink):
        self.Meds.set_imgLink(imgLink)