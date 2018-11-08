
class Medicine(object):
    def __init__(self):
        self.medID = None
        self.name = None
        self.type = type
        self.company = None
        self.qty = None
        self.price = None
        self.expDate = None
        self.shelf = None
        self.imgLink = None
        self.Builder = None

    class Builder(object):
        def __init__(self, medID=None, name=None, type=None, company=None, qty=None, price=None,
                     expDate=None, shelf=None, imgLink=None):
            self.medID = medID
            self.name = name
            self.type = type
            self.company = company
            self.qty = qty
            self.price = price
            self.expDate = expDate
            self.shelf = shelf
            self.imgLink = imgLink

        def build_medID(self, medID):
            self.medID = medID
            return self

        def build_name(self, name):
            self.name=name
            return self

        def build_type(self, type):
            self.type = type
            return self

        def build_company(self, company):
            self.company = company
            return self

        def build_qty(self, qty):
            self.qty = qty
            return self

        def build_price(self, price):
            self.price = price
            return self

        def build_ExpDate(self, ExpDate):
            self.expDate = ExpDate
            return self

        def build_shelf(self, shelf):
            self.shelf = shelf
            return self

        def build_imgLink(self, imgLink):
            self.imgLink= imgLink
            return self

        def build(self):
            med = Medicine()
            med.medID = self.medID
            med.name = self.name
            med.type = self.type
            med.company = self.company
            med.qty = self.qty
            med.price = self.price
            med.expDate = self.expDate
            med.shelf = self.shelf
            med.imgLink = self.imgLink
            return med

    def __str__(self):

        jsonTypeString =  '{"medID": "'+ self.medID+'", "name": "'+self.name+'", "' \
                          + 'type": "' + self.type + '", "' \
                          + 'company": "' + self.company + '", "' \
                          + 'price": "' + self.price + '", "' \
                          + 'qty": "' + self.qty + '", "' \
                          + 'expDate": "'+self.expDate+'", "' \
                        + 'shelf": "'+self.shelf+'", "'\
                        + 'imgLink": "'+self.imgLink+'"}'
        return jsonTypeString
