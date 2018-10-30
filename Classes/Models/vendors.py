

class Vendor(object):

    def __init__(self,venID,name,contact):
        self.venID = venID
        self.name = name
        self.contact = contact


    def __str__(self):

        jsonTypeString =  '{"venID": "'+ self.venID+'", "name": "'+self.name+'", "contact": "'+self.contact+'"}'

        return jsonTypeString



v1 = Vendor("v001", "Square Pharma Limited", "01XXXXXXXX")
v2 = Vendor("v002", "Beximco Pharma Limited", "01XXXXXXXX")
v3 = Vendor("v003", "Incepta Pharma Limited", "01XXXXXXXX")
v4 = Vendor("v004", "Aristopharma Limited", "01XXXXXXXX")
