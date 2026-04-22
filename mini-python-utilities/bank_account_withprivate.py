"""Build a simple Bank Account Management System to demonstrate OOP concepts in Python.This program compares two approaches:
1. Without private variables (balance is public).
2. With private variables and methods (balance is hidden and accessed safely)."""

class BankAccount:
    def __init__(self,holder,balance=0):
        self.holder=holder
        self.__balance=balance  # private variable
    def info(self):
        print(f'The name of account holder is {self.holder} and avaialble balance is {self.__balance}')
    def __checkamount(self,amount):         #private method 
        return amount >0
    def deposit(self,amount):
        if self.__checkamount(amount):
            self.__balance+=amount
            print(f'Hello {self.holder} your balance after deposit of {amount} is {self.__balance}')
    def withdraw(self,amount):
        if self.__checkamount(amount) and amount <=self.__balance:
            self.__balance-=amount
            print(f'The balance after withdrawl is {self.__balance}')
        if amount>self.__balance:
            print(f'Sorry {self.holder} you have  insufficent balance')
Customer1=BankAccount('Jay',0)
Customer2=BankAccount('Avi',1000)
Customer1.info()
Customer1.deposit(1000)
Customer2.info()
Customer2.withdraw(2000)

        
