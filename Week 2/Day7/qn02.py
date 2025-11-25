'''Create a class called BankAccount
Attributes (inside __init__):
account_number
account_holder
balance (default = 0)

Methods:
1️⃣ deposit(amount)
Add amount to balance
Reject negative or zero amounts
Print updated balance

2️⃣ withdraw(amount)
Allow only if enough balance
Reject negative or zero amounts
Print updated balance

3️⃣ check_balance()
Print current balance nicely

Your Task:
Create two bank accounts

Perform:
One deposit
One withdrawal
Check balance

Example (just for understanding):
You must NOT copy this—just understand:
Acc No: 123 → deposit 500 → withdraw 200 → balance 300
'''

class BankAccount:
    def __init__(self,account_no,account_holder,amount =0):
        self.account_no=account_no
        self.account_holder=account_holder
        self.amount=amount
    def deposit(self,amount):
        if amount>0:
            self.amount += amount
            print(f"Amount Deposited Succesfully !! your current Balance is{self.amount}")
        else:
            print("Min Deposit Atleast rs1 !! ")
    def withdraw(self,amount):
        if  amount>0:
            if self.amount>=amount:
                self.amount -=amount
                print(f"amouth withdrawl of {self.amount}")
            else:
                print("insifficient amount")
        else:
            print("-Ve Value entered..")
    def check_balance(self):
        print(self.amount)

bankacc1=BankAccount(123,"ritik",1000)
bankacc2=BankAccount(124,"raju")

print("bank details of AC 1")
bankacc1.deposit(1000)
bankacc1.withdraw(500)
bankacc1.check_balance()

print("bank details of AC 2")
bankacc2.deposit(1000)
bankacc2.withdraw(500)
bankacc2.check_balance()