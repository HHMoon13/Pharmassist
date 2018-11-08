
#order id, vandor name, total cost, paid amount, due amount, status, order date, due date
class Order(object):

    def __init__(self,orderID,companyName,totalCost,paid,due,status,orderDate,dueDate):
        self.orderID = orderID
        #self.order_id = order_id
        #self.venID = venID
        self.companyName = companyName
        self.totalCost = totalCost
        self.paid = paid
        self.due = due
        self.status = status
        #self.medName = medName
        #self.qty = qty
        self.orderDate = orderDate
        self.dueDate = dueDate


    def __str__(self):

        jsonTypeString =  '{"orderID": "'+ self.orderID+'", "companyName": "'+self.companyName+'", "' \
                          + 'totalCost": "' + self.totalCost + '", "' \
                          + 'paid": "' + self.paid + '", "' \
                          + 'due": "' + self.due + '", "' \
                          + 'status": "' + self.status + '", "' \
                          + 'orderDate": "'+str(self.orderDate)+'", "' \
                          + 'dueDate": "'+str(self.dueDate)+'"}'
        return jsonTypeString


    def stringData(self):
        data =  self.orderID + "#" + self.companyName + "#"+ str(self.totalCost) + "#" + str(self.paid) + "#" + str(self.due) +\
                "#" + self.status + "#" + str(self.orderDate) + "#" + str(self.dueDate)

        return data



# ####
# medNames=["Para01#Napa#Paracetamol#5#20#01-01-2020#22C#/static/Images/napa.jpg",
#           "Para02#Ace#Paracetamol#6#15#01-01-2020#22D#/static/Images/ace.jpg",
#           "Util01#Bandages#Utilities#2#50#01-01-2020#12B#/static/Images/bandages.jpg",
#           "Saline01#Orsaline#Saline#1#50#01-07-2019#11A#/static/Images/orsaline.jpg"
#           ]
# ####

