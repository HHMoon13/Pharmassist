
class Medicine(object):

    def __init__(self,medID,name,type,company=None,qty=None,price=None,
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


m1 = Medicine("Para01", "Napa", "Paracetamol", "Beximco Pharma Limited", "5", "20", "01-01-2020", "22C", "/static/Images/napa.jpg")
m2 = Medicine("Para02", "Ace", "Paracetamol", "Square Pharma Limited", "6", "15", "01-01-2020", "22D", "/static/Images/ace.jpg")
m3 = Medicine("Util01", "Bandages", "Utilities", "vendor1", "2", "50", "01-01-2020", "12B", "/static/Images/bandages.jpg")
m4 = Medicine("Saline01", "Orsaline", "Saline", "vendor2", "1", "50", "01-01-2020", "11A", "/static/Images/orslaine.jpg")
#m5 = Medicine("Para01#", "Napa", "Paracetamol", "5", "20", "01-01-2020", "22C", "/static/Images/napa.jpg")