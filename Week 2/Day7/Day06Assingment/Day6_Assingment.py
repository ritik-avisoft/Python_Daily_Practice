# BankAccount 

class BankAccount:
    """this calss hld the rec of bank acc""" # this is the doc for the bankAc cls
    def __init__(self, account_number, account_holder_name, balance=0):     #Everytime when i create an object(Account holder for this bank) this __init__ method call automatically to put the details for the acc holder with exactely valid parameter's.

        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposit successful! New Current Balance: ₹{self.balance}")
            past_transaction.append(f"Deposited Amout of {amount}")
        else:       #Disallowing the negative or zero values
            print("❌ Deposit amount must be positive!")
            past_transaction.append(f"Transaction failed Due to negative value")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"✅ Withdrawal successful! New Balance: ₹{self.balance}")
                past_transaction.append(f"Withdrawal Amout of {amount}")
            else:
                print("❌ Insufficient balance for withdrawal!")
                print(f"You current availavle balance is: {self.balance}")
                past_transaction.append(f"Withdrawal Amout of {amount} got Failed Due to Less Amount")
        else:
            print("❌ Withdrawal amount must be positive!")

    def check_balance(self):
        print(f"✅ Current Balance: ₹{self.balance}")


def list_of_action(input_acc_user):
    print(f"✅ Access granted to {input_acc_user}'s account.")
    print('''\nwhich action you want to perform?
        1. Withdraw Amout
        2. Deposit Money
        3. Check Balance''')
    action = input("Enter the action number (1/2/3): ")
    if action == '1':
        amount = float(input("Enter amount to withdraw: "))
        account1.withdraw(amount)
        
    elif action == '2':
        amount = float(input("Enter amount to deposit: "))
        account1.deposit(amount)
        
    elif action == '3':
        account1.check_balance()
        past_transaction.append(f"Balanced Check ")
    else:
        print("❌ Invalid action selected.")

# Creating 3 customer accounts
account1 = BankAccount("1230001801","Ritik kr Ranjan", 1000)
account2 = BankAccount("1230001802","Raj Sharma", 500)
account3 = BankAccount("1230001803","Anita Ranjan")

#Creating a user for each account to validate that no other person can have the access of another person's account
print('''
account1_user = "Ritik kr Ranjan"       #user for account1
account2_user = "Raj Sharma"            #user for account2
account3_user = "Anita Ranjan"          #user for account3
''')

# Class Attributes -> 
# print(BankAccount.__base__)
# print(BankAccount.__bases__)
# print(BankAccount.__doc__) # hold the doc's for any cls 
# print(BankAccount.__dict__)
past_transaction =[]
trans_flag=True
proceed = 'yes'

while proceed.lower() == 'yes':
    input_acc_user = input("Enter the account holder name to access your account: ")
    if input_acc_user == "Ritik kr Ranjan":
        list_of_action(input_acc_user) #Calling the function to perform action for input_acc_user
    elif input_acc_user == "Raj Sharma":
        list_of_action(input_acc_user)
    elif input_acc_user == "Anita Ranjan":
        list_of_action(input_acc_user)
    else:
        print("❌ Unauthorized access to a`ccount!!")
        trans_flag=False
        break
    
    proceed = input("Do you want to perform another transaction? (yes/no): ")

# print("\n🧾 Transaction History:")
# if trans_flag:
#     for transaction in past_transaction:
#         print(f"- {transaction}")
# else:
#     print("No Transaction's")
#     print("Try With Correct Banking Detail's.. ")

print("\nThank you for banking with us! Have a great day! 😊")
    





'''
Area of improvement :- 
-> while depositing amt only int is acceptable , but right now while giving input rather than int it;s giving err which is not understandable for user 
-> same for withdrawl only accept int value

'''


