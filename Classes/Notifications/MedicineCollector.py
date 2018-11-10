from Classes.Models.MedicineBuilder import Medicine
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm

class MedicineCollector(object):

    def __init__(self):
        self.medicines = []

    def createMedList(self):

        # medFromDatabase = [ "Saline01#Orsaline#Saline#1#50#01-07-2019#11A#/static/Images/orsaline.jpg",
        #                       "Util01#Bandages#Utilities#2#50#01-01-2020#12B#/static/Images/bandages.jpg"]
        medFromDatabase = []
        a = adm.AccessDatabaseMedicines().getIterator()
        while a.hasNext():
            medFromDatabase.append(a.next())

        for med in medFromDatabase:
            #print(med)
            medAttrs = med.split("#")
            medicine= Medicine.Builder().build_medID(medAttrs[0]) \
                .build_name(medAttrs[1]) \
                .build_type(medAttrs[2]) \
                .build_company(medAttrs[3]) \
                .build_price(medAttrs[4]) \
                .build_qty(medAttrs[5]) \
                .build_ExpDate(medAttrs[6]) \
                .build_shelf(medAttrs[7]) \
                .build_imgLink(medAttrs[8])\
                .build()

            self.medicines.append(medicine)

        return self.medicines

# m = MedicineCollector()
# l = m.createMedList()
# for li in l:
#  print(li)