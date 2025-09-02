# This class models a simple bank account using Object-Oriented Programming principles.
# It encapsulates the account data such as balance and account number.
# It provides methods to debit and credit money,
# while hiding the internal balance update details from the user (abstraction).
# It also includes a getter method to view the current balance safely.


class Account:
    def __init__(self, bal, acc_no):
        self.balance=bal
        self.account_no=acc_no
        
    def debit(self, amount):
        self.balance-=amount
        print("Rs." , amount, "was debited")
        print("Total balance: ",self.get_balance())
        
    def credit(self, amount):
        self.balance+=amount
        print("Rs.", amount, "was credited")
        print("Total balance: ",self.get_balance())

        
    def get_balance(self):
        return self.balance
        
        
acc1=Account(100000,12345)
acc1.credit(30000)
acc1.debit(20000)
        
   