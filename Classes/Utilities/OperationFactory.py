from Classes.MedicineAdditionClasses import Add, Remove, Update, NoOperation
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm
from Classes import Statics

class OperationFactory:
    def getOperation(self, msg):
        temp = msg.split("#")
        toSend=""
        i=0
        while i<temp.__len__():
            if i==0:
                i+=1
                continue
            toSend+=temp[i]+"#"
            i+=1
        #print(temp[0], toSend)
        if temp[0]=="add":
            if temp.__len__() < 10:
                toSend += Statics.imageLink
            Statics.imageLink="/static/Images/generic.png"
            Statics.medicineOperation=toSend
            return Add.Add()
        elif temp[0]=="remove":
            toSend = int(toSend[:-1])
            Statics.medicineOperation=toSend
            return Remove.Remove()
        elif temp[0]=="change":
            Statics.medicineOperation=toSend
            return Update.Update()
        else:
            return NoOperation.NoOperation()