from Classes.Models.MedicineBuilder import Medicine
from Classes.DatabaseHandlers.dataFetcher import fetchMedicines

class MedicineCollector(object):

    def __init__(self):
        self.medicines = []

    def createMedList(self):

        medFromDatabase = fetchMedicines()

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
# i = 1
# for li in l:
#  print(str(i)+": "+li.name)
#  i+=1