"""Build a simple Bank Account Management System to demonstrate OOP concepts in Python.This program compares two approaches:
1. Without private variables (balance is public).
2. With private variables and methods (balance is hidden and accessed safely)."""

class BankAccount:
    def __init__(self,holder,balance=0):
        self.holder=holder
        self.balance=balance  # public variable
    def info(self):
        print(f'The name of account holder is {self.holder} and avaialble balance is {self.balance:}')
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'Hello {self.holder} your balance after deposit of {amount} is {self.balance}')
    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance-=amount
            print(f'The balcnce after withdrawl is {self.balance}')
        if amount>self.balance:
            print(f'Sorry {self.holder} you have  insufficent balance')
Customer1=BankAccount('Jay',25000)
Customer2=BankAccount('Avi',1000)
Customer1.info()
Customer1.deposit(1000)
Customer2.info()
Customer2.withdrawl(2000)

        
