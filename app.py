import os
from flask import *
from Classes.Utilities import Iterator
from Classes.DatabaseAccessors import AccessDatabaseMedicines as adm, AccessDatabaseAccounts as ada, AccessDatabaseVendors as adv, AccessDatabaseExpenses as ade, AccessDatabaseSellings as ads
from Classes import Statics
import Classes.DatabaseHandlers.fetch
from Classes.Notifications import MedicineList
from Classes.Models import *
from Classes.ManageOrders import CompanyList as companyList
from Classes.ManageOrders import medOrderList as medOrderList
from Classes.ManageOrders import OrderList as OrderList
from Classes.Utilities import OperationFactory
from Classes.Utilities import ResponseContext, ResponseState as Response
from Classes.AuthenticationResponses import OKState, WrongUsernameState, WrongPasswordState, InitialState
from Classes.DecoratorPatternFiles.BaseMedicines import BaseMedicines
from Classes.DecoratorPatternFiles.DecoratorMedicine import DecoratorMedicine
from Classes.Models import medOrders
from Classes.ManageOrders import CompanyList as companyList
from Classes.ManageOrders import medOrderList as medOrderList
from Classes.ManageOrders.makeOrder import makeOrder
from Classes.ManageOrders import OrderList as OrderList
from Classes.Utilities import OperationFactory
import json



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)

r0 = InitialState.InitialState()
rc = ResponseContext.ResponseContext(r0)
rc.respondToState("", "")

@app.route('/')
def startupPage():
    response=Statics.authMessage
    print(response)
    return render_template('signInPage.html', response=response)

@app.route('/home')
def homepage():
    usr=Statics.currentUser
    return render_template('homepage.html', usr=usr)

@app.route('/aboutUs')
def aboutUsPage():
    return render_template('aboutUsPage.html')

@app.route('/finances', methods=['GET', 'POST'])
def financesPage():
    sellList = []
    a = Iterator.Iterator
    a = ads.AccessDatabaseSellings().getIterator()
    while a.hasNext():
        sellList.append(a.next())
    expenseList = []
    b = Iterator.Iterator
    b = ade.AccessDatabaseExpenses().getIterator()
    while a.hasNext():
        expenseList.append(b.next())
    return render_template('finances.html', sellList=sellList, expenseList=expenseList)

@app.route('/finances_second', methods=['GET', 'POST'])
def finances_secondPage():
    sellList = []
    a = Iterator.Iterator
    a = ads.AccessDatabaseSellings().getIterator()
    while a.hasNext():
        sellList.append(a.next())
    expenseList = []
    b = Iterator.Iterator
    b = ade.AccessDatabaseExpenses().getIterator()
    while a.hasNext():
        expenseList.append(b.next())
    return render_template('finances_second.html', sellList=sellList, expenseList=expenseList)

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

@app.route('/medicineListModify', methods=['POST', 'GET'])
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
    searchResults = a.search(Statics.searchKey)
    print(searchResults)
    return render_template('searchResults.html', searchResults = searchResults)


@app.route('/searchHandler', methods=['POST'])
def search():
    Statics.searchKey=""
    searchRequest = request.get_json(force=True)
    print(searchRequest)
    for i in searchRequest:
        Statics.searchKey += str(i['queried'])
    return 'OK'

@app.route('/medChange', methods=['POST'])
def medChange():
    temp=""
    changeRequest = request.get_json(force=True)
    a = Iterator.Iterator
    a = adm.AccessDatabaseMedicines().getIterator()
    for i in changeRequest:
        temp += str(i['change'])
    opF = OperationFactory.OperationFactory().getOperation(temp)
    opF.doOperation(Statics.medicineOperation)
    return 'OK'


@app.route('/authCheck', methods=['POST'])
def update():
    Statics.currentUser = ""
    currentUser = request.get_json(force=True)
    temp=""
    for i in currentUser:
        temp+=str(i['userpass'])
    receivedData = temp.split("#")
    username=receivedData[0]
    password=receivedData[1]
    userList = []
    a = Iterator.Iterator
    a = ada.AccessDatabaseAccounts().getIterator()
    while a.hasNext():
        userList.append(a.next())

    isUsernameValid=False

    r0 = InitialState.InitialState()
    r1 = OKState.OKState()
    r2 = WrongPasswordState.WrongPasswordState()
    r3 = WrongUsernameState.WrongUsernameState()

    rc = ResponseContext.ResponseContext(r0)
    rc.respondToState("", "")

    #id, username, password, fullname, usertype

    for i in userList:
        temp2 = i.split("#")
        userType = temp2[4]
        if temp2[1]==username and temp2[2]==password:
            rc.setState(r1)
            rc.respondToState(username, userType)
            isUsernameValid=True
            break
        if temp2[1]==username and temp2[2]!=password:
            rc.setState(r2)
            rc.respondToState(username, userType)
            isUsernameValid=True
            break

    if isUsernameValid==False:
        rc.setState(r3)
        rc.respondToState(username, "")

    response=Statics.authMessage
    print(response)
    return render_template('signInPage.html', response=response)

@app.route('/signout')
def signout():
    r0 = InitialState.InitialState()
    rc = ResponseContext.ResponseContext(r0)
    rc.respondToState("", "")
    print(Statics.authMessage)
    print("Signed Out")
    return redirect("/", 302)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/imageUpload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(app.root_path+"/static/Images/"+filename)
            Statics.imageLink='/static/Images/'+filename
    return 'OK'

#
@app.route('/orders')
def ordersPage():
    order = OrderList.OrderList()
    mediOrder = medOrderList.medOrderList()
    #order.mapOrder()
    return render_template('orders.html',orderlist = order.get_ordersList(),medOrderList = mediOrder.get_medordersList())

@app.route('/munia', methods=['POST' ])
def receive_munia():
    if request.method == 'POST':
        print(request.form)
        data= request.form
        print(data)
        paid = data['paid']
        makeOrder.generateOrder(data)
        print(paid)
        return redirect('/orders')

@app.route('/updateOrder', methods=['POST' ])
def update_order():
    if request.method == 'POST':
        data = request.form
        print(data)
        print(data['orderID'])
        makeOrder.updateOrder(data)

        return ordersPage()


@app.route('/recieveCompanyName', methods=['POST'] )
def recieve_companyName():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(len(data))

        makeOrder.setCompanyName(data["companyName"])
        return ordersPage()

@app.route('/recieveMedOrders', methods=['POST'])
def receive_orderData():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(data)
        res = makeOrder.addItem(data)
        print(res)
        return str(res)
       # orderID, order_id, venID, companyName, medName, qty, dueDate, status, cost)
        #print(request.form)
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
   # temp =request.form['mydata']

   if request.method == "POST":
       temp = request.form["mydata"]
       list = temp.split("#")
       if temp == "":
           return "0"
       print(temp)
       print(list)


       cnt = 0
       for i in list:
           x = i.split("*")
           if cnt == 0:
               m = BaseMedicines(x[2], x[4])
           else:
               m = DecoratorMedicine(m, x[2], x[4])
           cnt = cnt + 1



       result = m.get_cost()
       print(str(result))
       return str(result)
    #Statics.currentReceipt=temp
    #x=temp.split("#")
    #here the values to be inserted in table sellings are in this form - Money*Date*Item*CashierName*Quantity in the x array
    #Date is in YYYY-MM-DD format
    #print(x)
@app.route('/testing')
def testpage():
    #test=Statics.currentReceipt
    # return render_template('newFeature.html',test=test)
    return render_template('newFeature.html')



if __name__ == '__main__':
    app.run()