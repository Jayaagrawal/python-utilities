#Name Mangling
class BankAccount:
    def __init__(self,holder,balance):
        self.holder=holder
        self.__balance=balance      #mangled attribute
    def balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance+=amount
        return self.__balance
    def withdraw(self,amount):
        self.__balance-=amount
        return self.__balance
    
#Create object
account=BankAccount('Nick',15000)
#Access through method (recommended)
print('The current account balance is ',account.balance())
print('The amount after withdrawl is ',account.withdraw(1000))
#try to access private variable directly which will fail
try:
    print(account.__balance)
except AttributeError as e:
    print('Error',e)
# Access using mangled name (not recommended but possible)
print('Balance via mangled name is ',account._BankAccount__balance)






