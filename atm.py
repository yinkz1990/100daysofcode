from time import sleep
#pincode is any 4 digit number
print("You are welcome to YK Bank")
for x in range(4):
    pincode = int(input("Enter your password:"))
    break
class BankAccount:
    def __init__(self):
        self.balance=0 
        self.choice=0
        self.action = 0
    
    def option(self):
        opt = float(input("Do you want to perform another transaction? Enter 1 to continue and 0 to exit-:"))
        if(opt == 1):
            self.dashboard()
        elif(opt == 0):
            print("Thank You for using This ATM Machine")
            print("You can take your card")
        sleep(3)
        exit()              
    def dashboard(self):
        print ("1  >>Deposit         2  <<Withdraw")
        print ("3  >>Recharge        4  <<Check Balance")
        resp = int(input("Please enter a response-:"))
        self.choice = resp
        if(self.choice == 1):
            self.deposit()
        elif(self.choice == 2):
            self.withdraw()
        elif(self.choice == 3):
                self.airtime()
        elif(self.choice == 4):
            self.check_balance()
        else:
            print("This is not a valid option")
       
        
    def deposit(self): 
        amount = float(input("Enter the amount to be deposited:")) 
        self.balance +=amount
        print("Amount deposited:",amount)
        print("")
        self.option()
        
    def withdraw(self): 
        amount = float(input("Enter the amount to be withdrawn:"))
        if self.balance >= amount:
            self.balance -=amount
            print("\n You have withdrawn", amount)
        elif self.balance < amount:
            print("Insufficient balance, pls check your balance and retry")
        print("")
        self.option()  
    def airtime(self):
        mobile_number = str(input("Enter the phone number-:"))
        while len(mobile_number) !=11:
            print("Enter a valid number")
        amount = float(input("Enter the amount:"))
        if self.balance >= amount:
            self.balance -=amount
            print("\n You have creditted", mobile_number,"with:",amount)
            
        else:
            print("\n insufficient balance, pls check your balance and retry")
            
        print("")
        self.option()
    def check_balance(self):
        print("Your net Available Balance =",self.balance)
        print("")
        self.option()
    
    
         

s = BankAccount()
s.dashboard()
s.deposit()
s.withdraw()
s.airtime()
s.check_balance()
