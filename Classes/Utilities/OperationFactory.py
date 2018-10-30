from Classes.MedicineAdditionClasses import Add, Remove, Update
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes import Statics

class OperationFactory:
    def executeOperation(self, msg):
        temp = msg.split("#")
        toSend=""
        i=0
        while i<temp.__len__():
            if i==0:
                i+=1
                continue
            toSend+=temp[i]+"#"
            i+=1
        print(temp[0], toSend)
        if temp[0]=="add":
            a = Add.Add().doOperation(toSend)
            if temp.__len__() < 10:
                toSend += "/static/Images/generic.png"
            Statics.medList.append(toSend)
            #uporer line hobe na final product e
        elif temp[0]=="remove":
            a = Remove.Remove().doOperation(toSend)
        elif temp[0]=="change":
            a = Update.Update().doOperation(toSend)