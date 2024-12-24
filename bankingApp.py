import math
print("welcome to the online banking application")
def signin():
    global name # username 
    global pin # password
    global cb # current balance
    name = str(input("Please create your username"))
    pin = str(input("please create your 6 digits pin"))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin has to be in 6 digits")
        newpin = str(input("please create your 6 digits pin"))
        if len(newpin) != 6:
             print("The pin has to be in 6 digits")
             signin()
        else:
            pin = newpin
    print("Thanks for creating your bank account")

def forgotpin():
    recoverpin = str(input("please create your new 6 digits pin"))
    if len(recoverpin) !=6:
        print("the pin has to be in 6 digits")
        forgotpin()
    else:
        print("the new pin has been stored, please log in")
        pin = recoverpin
        login()


def depositinterest(p,r,t):
    # A = pe^(rt) which is the formula for calculating the compound interest
    p = float(p)
    r = float(r)
    t = float(t)
    rt = r * t
    e = math.exp(rt)
    # calculation
    a = p * e # future value of your investment
    return a

def login():
    # make1 represent username
    # pin1 represent user's pin
    name1 = str(input("Please enter your username"))
    pin1 = str(input("Please enter your pin"))
    # check if the name and pin matched
    if name1 == name and pin1 == pin:
        print("welcome to the online banking application" + " " + name)
        print("please choose the menu downhere")
        listmenu = ["1-Deposit","2-Withdraw","3-Transfer","4-Check balance","5-Deposit interest rate","6-Calculate compound interest"]
        for b in listmenu:
            print(b)
        choose = int(input("please enter number of your choice"))
        d = 0 # d represents deposit
        w = 0 # w represents withdrawal
        cb = 0 # cb represents current balance
        if choose == 1:
            d = int(input("Enter the Amount of your Deposit"))
            cb = d
            print("Your current balance is" +" "+ str(cb))
        elif choose == 2:
            w = int(input("Enter the amount of money that you want to withdraw"))
            if w > cb:
                print("Your current balance is not sufficient forthis transaction")
                login()
            else:
                cb = d-w
                print(str(w) +" "+ "has been withdrawn from your account" +" "+ " and your current balance is" + " " + str(cb))
        elif choose == 3:
            dest = str(input("Please enter the account number of receiver in 8 digits"))
            if len(dest) == 8:
                amount = int(input("Please enter the amount of money you want to transfer"))
                if amount > cb:
                    print("Your current balance is not sufficient for this transaction")
                    login()
                else:
                    cb = d - amount
                    print("The transaction of" + " " +str(amount) + " " + "has been transfered to" + " " + str(dest) + " " + " your current balance is" + str(cb))    
            else:
                print("The transaction has been rejected since the destination account is in valid")
                login() 
        elif choose == 4:
            print("Your current balance is" +" " + str(cd))
        elif choose == 5:
            if d > 50000:
                rate = 3 
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
            print("Your current deposi interest rate is" +" "+ str(rate) + "%")
        elif choose == 6:
            listoption = ["1-Calculate your deposit compound interest based on your CB","2-Calculate your deposit compound interest based on your deposit input"]
            for n in listoption:
                print(n)
            choice = int(input("Please enter your choice from the options above"))
            if choice == 1:
                timing = str(input("How many years do you want to invest your money"))
                if d > 50000:
                    ratex = 3/100
                elif d >30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print("Your current balance in" + " " + "timing" + "years will be")
                print(depositinterest(cb,ratex,timing))
            elif choose == 2:
                timing = str(input("How many years do you want to invest your money"))
                money = str(input("Please enter the amount of money you would like to deposit"))
                money = int(money)
                if d > 50000:
                    ratex = 3/100
                elif d >30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print("Your current balance in" + " " + "timing" + "years will be")
                print(depositinterest(money,ratex,timing))
        else:
            print("Option is not available, Back to main menu")
            login()


    else:
        print("either of your username or pin is wrong, did you create your account")
        list1 = ["1-yes","2-no"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice below"))
        if inp == 1:
            list2 = ["1-do you want to attempt to log in again?","2-you forgot your pin"]
            for e in list2:
                print(e)
            theanswer = str(input("Please enter your choice"))
            theanswer = int(theanswer)
            if theanswer == 1:
                login()
            elif theanswer == 2:
                forgotpin()
            else:
                print("option mot available")
                login()
        elif inp == 2:
            print("Please create your account")
            signin()
    
def mainmenu():
    optionone = int(input("Choose 1 to sign in and Choose 2 to log in"))
    if optionone == 1:
        signin()
    elif optionone == 2:
        login()
    else:
        print("Option is not available")
        mainmenu()
    exit()

def exit():
    answer = str(input("Do you still want to conduct transaction? Yes or No"))
    if answer == "Yes":
        login()
    elif answer == "No":
        print("thank you for using this app")
    else:
        print("option is not available")
        mainmenu()
            
mainmenu()


    