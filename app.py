from flask import *
from Classes.Utilities import Iterator
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm, AccessDatabaseAccounts as ada, AccessDatabaseVendors as adv
from Classes import Statics
import Classes.DatabaseHandlers.fetch
from Classes.Notifications import MedicineList
from Classes.Models import *
from Classes.ManageOrders import CompanyList as companyList
from Classes.ManageOrders import medOrderList as medOrderList
from Classes.ManageOrders import OrderList as OrderList

app = Flask(__name__)


@app.route('/')
def startupPage():
    response=Statics.authMessage
    return render_template('signInPage.html', response=response)

@app.route('/home')
def homepage():
    usr=Statics.currentUser
    return render_template('homepage.html', usr=usr)

@app.route('/aboutUs')
def aboutUsPage():
    return render_template('aboutUsPage.html')

@app.route('/finances')
def financesPage():
    return render_template('finances.html')

@app.route('/makeReceipt')
def makeReceiptPage():
    medNames = []
    a = Iterator.Iterator
    a = adm.AccessDatabaseMedicines().getIterator()
    while a.hasNext():
        medNames.append(a.next())
    usr=Statics.currentUser
    return render_template('makeReceipt.html', medNames=medNames,usr=usr)

@app.route('/medicines')
def medicinesPage():
    medList=[]
    a = Iterator.Iterator
    a = adm.AccessDatabaseMedicines().getIterator()
    while a.hasNext():
        medList.append(a.next())
    return render_template('medicines.html', medList=medList)

@app.route('/medicineListModify')
def medListModifyPage():
    medList = []
    a = Iterator.Iterator
    a = adm.AccessDatabaseMedicines().getIterator()
    while a.hasNext():
        medList.append(a.next())
    return render_template('medicineListEdit.html', medList=medList)

@app.route('/notifications')
def notificationsPage():
    m = MedicineList.MedicineList()
    notiList = [] #list of strings
    for x in m.sendNotifications():
        notiList.append(x)

    print(notiList)
    return render_template('notifications.html', notiList=notiList)


@app.route('/accounts')
def accountsPage():
    currentUser = Statics.currentUser
    currentUserType = Statics.currentUserType
    accountList = []
    a = Iterator.Iterator
    a = ada.AccessDatabaseAccounts().getIterator()
    while a.hasNext():
        accountList.append(a.next())
    print(accountList)
    return render_template('accounts.html', currentUserType=currentUserType, accountList=accountList)


@app.route('/companies')
def companiesPage():
    vendorList = []
    a = Iterator.Iterator
    a = adv.AccessDatabaseVendors().getIterator()
    while a.hasNext():
        vendorList.append(a.next())
    return render_template('companies.html', vendorList=vendorList)


@app.route('/addCompany')
def newCompanyPage():
    vendorList = []
    a = Iterator.Iterator
    a = adv.AccessDatabaseVendors().getIterator()
    while a.hasNext():
        vendorList.append(a.next())
    return render_template('newCompanyPage.html', vendorList=vendorList)

@app.route('/newUser')
def newUserPage():
    accountList = []
    a = Iterator.Iterator
    a = ada.AccessDatabaseAccounts().getIterator()
    while a.hasNext():
        accountList.append(a.next())
    return render_template('newUser.html', accountList=accountList)


@app.route('/addNewUser', methods=['POST'])
def addNewUser():
    message=""
    temp = request.get_json(force=True)
    for i in temp:
        message += str(i['message'])
    Statics.userList.append(message)

@app.route('/addCompanyHandler', methods=['POST'])
def addNewCompany():
    message=""
    temp = request.get_json(force=True)
    for i in temp:
        message += str(i['comp'])
    Statics.vendorList.append(message)


@app.route('/searchResults')
def resultsPage():
    Statics.searchResult=""
    a = Iterator.Iterator
    a = adm.AccessDatabaseMedicines().getIterator()
    searched = a.search(Statics.searchKey)
    return render_template('searchResults.html', searched = searched)


@app.route('/searchHandler', methods=['POST'])
def search():
    Statics.searchKey=""
    searchRequest = request.get_json(force=True)
    for i in searchRequest:
        Statics.searchKey += str(i['queried'])

@app.route('/medChange', methods=['POST'])
def medChange():
    temp=""
    changeRequest = request.get_json(force=True)
    a = Iterator.Iterator
    a = adm.AccessDatabaseMedicines().getIterator()
    for i in changeRequest:
        temp += str(i['change'])
    temp2=temp.split("#")
    if temp2[0]=="add":
        print(temp2)
        temp3=""
        for i in temp2:
            if i!="add":
                temp3+=i+"#"
        if temp2.__len__()<10:
            temp3+="/static/Images/generic.png"
        Statics.medList.append(temp3)
        a.add(temp3)
    elif temp2[0]=="remove":
        a.remove(temp2[1])
    elif temp2[0]=="change":
        print(temp2)
        a.update(temp2[1], temp2[2], temp2[3])


@app.route('/authCheck', methods=['POST'])
def update():
    Statics.currentUser = ""
    currentUser = request.get_json(force=True)
    temp=""
    for i in currentUser:
        temp+=str(i['userpass'])
    b = temp.split("#")
    username=b[0]
    password=b[1]
    userList = []
    a = Iterator.Iterator
    a = ada.AccessDatabaseAccounts().getIterator()
    while a.hasNext():
        userList.append(a.next())

    isValid=False

    #id, username, password, fullname, usertype

    for i in userList:
        temp2 = i.split("#")
        if temp2[1]==username and temp2[2]==password:
            Statics.authMessage="OK"
            Statics.currentUser=username
            Statics.currentUserType=temp2[4]
            isValid=True
            break
        if temp2[1]==username and temp2[2]!=password:
            Statics.authMessage="Wrong Password"
            isValid=True
            break

    if isValid==False:
        Statics.authMessage="Wrong Username"

    response=Statics.authMessage
    print(response)
    return render_template('signInPage.html', response=response)

#
@app.route('/orders')
def ordersPage():
    order = OrderList.OrderList()
    mediOrder = medOrderList.medOrderList()
    return render_template('orders.html',orderlist = order.get_ordersList(),medOrderList = mediOrder.get_medordersList())

@app.route('/munia', methods=['POST' ])
def receive_munia():
    if request.method == 'POST':
        print(request.form)
        return ordersPage()

@app.route('/orders/placeOrder', methods=['POST'])
def placeOrderPage():
    v = companyList.CompanyList()
    m = MedicineList.MedicineList()

    # v.printList()
    print(v.vendorsList())
    print(m.mediList())
    return render_template('placeOrder.html', vendorslist=v.vendorsList(), medList=m.mediList())


#
@app.route('/addreceipt', methods=['POST'])
def receipt():
    temp =request.form['mydata']
    Statics.currentReceipt=temp
    x=temp.split("#")
    #here the values to be inserted in table sellings are in this form - Money*Date*Item*CashierName*Quantity in the x array
    #Date is in YYYY-MM-DD format
    print(x)

@app.route('/testing')
def testpage():
    #test=Statics.currentReceipt
    # return render_template('newFeature.html',test=test)
    return render_template('newFeature.html')



if __name__ == '__main__':
    app.run()