class Bank_Account:
    """self parameter is used to represent the instance of the class.
    It is also used to access the variables and methods from a class
    when the object is created it wll pass to the class's first argument which is self 
    """
    def __init__(self,accountNo,account_name,ifsc_code,balance):
        self.accountNo=accountNo
        self.account_name=account_name
        self.ifsc_code=ifsc_code
        self.balance=balance
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=self.amount
            print(f"Your Amount {self.amount} withdrawed Successfully")
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount 
        print(f"Your Amount {self.amount} deposited Successfully ")
        
    def check_balance(self):
        print("The current balance is:",self.balance)
    def display(self):
        print(self.account_name ,self.accountNo,self.ifsc_code,self.balance)
#have to give arguments
obj1=Bank_Account(12345678910,"sirisha","IFSC98759",10000)
obj1.deposit(5000)
obj1.withdraw(10000)
obj1.withdraw(10000)
obj1.check_balance()
obj1.display()