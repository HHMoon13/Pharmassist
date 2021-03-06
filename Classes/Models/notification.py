
class Notification(object):

    def __init__(self,notiID,type,medName,medID, medShelf = "",status="unread"):
        self.notiID = notiID
        self.type = type
        self.medName  = medName
        self.medID  = medID
        self.medShelf = medShelf
        self.status = status

    def getShortString(self):
        notiStr = self.medName ;
        if self.type == "Empty":
            notiStr += " is out of stock!"
        elif self.type == "Expired":
            notiStr += " date expired!"
        return notiStr

    def getNotiString(self):
        notiStr = self.medName +" ["+str(self.medID)+", at Shelf: "+self.medShelf+"]"
        if self.type=="Empty":
            notiStr += " is out of stock!"
        elif self.type=="Expired":
            notiStr += " date expired. Please remove from shelf."
        return notiStr

    def __str__(self):

        jsonTypeString =  '{"medID": "'+ str(self.medID)+'",' \
                          +'"medName": "'+self.medName+'", "notiString": "'\
                          +self.getNotiString()\
                          +'", "type": "' + self.type + '", "' \
                          +'status": "'+self.status+'"}'
        return jsonTypeString

# n = Notification(1,"Empty","Napa",30,"22C","unread")
# new_noti = Notification(notiID=notiID,
#                                 type="Expired",
#                                 medName=medName,
#                                 medID=medID,
#                                 medShelf=medShelf,
#                                 status="Unread")