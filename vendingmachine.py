# You are tasked to code the vending machine logic out using Python Programming Language. 
# In your code, you can have a few drinks as your items with any price (no coin).
# The customer should be able to insert any notes to buy his preferred drinks.
# The outcome is to release the least amount of notes back to the customer. 

productList = [
        {"id": 1, "name": "Coke", "price": 5, "currency": "RM"},
        {"id": 2, "name": "100Plus", "price": 3, "currency": "RM"},
        {"id": 3, "name": "Pepsi", "price": 1, "currency": "RM"}
        ]

actionList = [
        {"id": 1, "name": "Pay", "desc": "Proceed to make payment."},
        {"id": 2, "name": "Add Drinks", "desc": "Add more drinks."},
        {"id": 3, "name": "Cancel", "desc": "Cancel order."}
        ]
        
totalPrice = 0;

# Function - START
def displayVendingMachine():
    print("Choose any drink. ")
    for product in productList:
        print(product["id"], ") " + product["name"] + ": "+ product["currency"], product["price"], sep="")
    
    selectProduct()

def selectProduct():
    global totalPrice
    totalPriceTemp = 0
    
    productSelected = int(input("Please select a drink (Enter the number of the drinks. eg: 1): "))
    qtyInsert = int(input("Please insert quantity of drink: "))
    
    cart = filter(lambda x: x["id"] == productSelected, productList)
    
    for c in cart:
        totalPriceTemp = c["price"] * qtyInsert
        totalPrice = totalPrice + totalPriceTemp
        
    displayAction()

def displayAction():
    print("Choose any action. ")
    for action in actionList:
        print(action["id"], ") " + action["desc"], sep="")
    actionID = int(input("Choose an action to perform? : "))
    
    if(actionID == 1):
        calculateBalance()
    elif(actionID == 2):
        selectProduct()
    elif(actionID == 3):
        quit()
    else: 
        displayAction()

def calculateBalance(): #Check note return
    print("Total Price: RM", totalPrice)
    amtInsert = int(input("Please enter amount of cash insert (RM): "))
    
    while (amtInsert < totalPrice):
        amtReInsert = int(input("Insufficient amount. Please insert more cash (RM): "))
        amtInsert = amtInsert + amtReInsert
    
    note100 = 0;
    note50 = 0;
    note20 = 0;
    note10 = 0;
    note5 = 0;
    note1 = 0;
    
    amtLeft = amtInsert - totalPrice
    while(amtLeft > 0):
        if(amtLeft >= 100):
            amtLeft = amtLeft - 100;
            note100 = note100 + 1;
        elif(amtLeft >= 50):
            amtLeft = amtLeft - 50;
            note50 = note50 + 1;
        elif(amtLeft >= 20):
            amtLeft = amtLeft - 20;
            note20 = note20 + 1;
        elif(amtLeft >= 10):
            amtLeft = amtLeft - 10;
            note10 = note10 + 1;
        elif(amtLeft >= 5):
            amtLeft = amtLeft - 5;
            note5 = note5 + 1;
        elif(amtLeft >= 1):
            amtLeft = amtLeft - 1;
            note1 = note1 + 1;
        else:
            print("Empty")
    
    print("Amount Received: RM", amtInsert)
    print("Balance: RM", amtInsert - totalPrice)
    print("RM100 note: ", note100)
    print("RM50 note: ", note50) 
    print("RM20 note: ", note20) 
    print("RM10 note: ", note10) 
    print("RM5 note: ", note5) 
    print("RM1 note: ", note1)
    isAgain()

def isAgain():
    retry = input("Do you want to buy again (Y/N)?")
    if(retry == "Y"):
        displayVendingMachine()
    if(retry == "N"):
        quit()
    else:
        isAgain()
    
# Function - End

displayVendingMachine()