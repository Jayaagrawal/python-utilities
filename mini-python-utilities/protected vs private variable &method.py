# Protected vs private varibales and methods to demonstrate encapsulation
class Bankaccount:
    def __init__(self,holder,balance,account_type):
        self.holder=holder
        self._account_type=account_type     #protected varibale (single underscore)
        self.__balance=balance              # private varibale (double underscore) 
    def show_balance(self):
        return self.__balance
    def holder_detail(self):
        return self.holder
    
b=Bankaccount('jaya',1000,'saving')
print(b.show_balance())
print(b.holder_detail())


