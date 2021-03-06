from Classes import Statics


class medOrder(object) :

    def __init__(self,orderID,order_id,venID,companyName,medName,qty,dueDate,status,cost):

        self.order_id = order_id
        self.venID = venID
        self.cost = cost
        self.medName = medName
        self.qty = qty
        self.orderID = orderID
        self.companyName = companyName
        self.dueDate = dueDate
        self.status = status


    def __str__(self):
        jsonTypeString = '{"orderID": "' + self.orderID + '", "order_id": "' + self.order_id + '", "' \
                         + 'venID": "' + self.venID + '", "' \
                         + 'companyName": "' + self.companyName + '", "' \
                         + 'medName": "' + self.medName + '", "' \
                         + 'qty": "' + str(self.qty) + '", "' \
                         + 'dueDate": "' + str(self.dueDate) + '", "'\
                         + 'status": "' + str(self.status) + '", "' \
                         + 'cost": "' + self.cost + '"}'

        return jsonTypeString


    def medOrderList(self):
        med = []
        medorder = Statics.medorder  # [] #list of objects, will be collected from database

        for item in medorder:
            # print(item)
            sp = str(item).split('#')
            # print(len(sp))
            m = medOrder(sp[0], sp[1], sp[2], sp[3], sp[4], sp[5], sp[6], sp[7], sp[8])
            med.append(m)


        return med

    def medordersList(self):
        orderlist = self.medOrderList()
        list = []
        for item in orderlist:
            list.append(item.__str__())

            #  "\"" +str(item.venID) + "\" : "+         "\"items\" : "

        return list

    #orderID,order_id,venID,companyName,medName,qty,dueDate,status,cost):
    def stringData(self):
        data =  str(self.orderID) + "#" + self.order_id + "#"+ self.venID + "#" + self.companyName + "#" + self.medName +\
                "#" + str(self.qty) + "#" + str(self.dueDate) + "#" + self.status + "#" + str(self.cost)

        return data