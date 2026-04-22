#- Random List Generator
#Problem: Build a program that generates a list of n random integers between a user-defined range (say a to b). Print the list.



import random
a=int(input("Enter the starting number for the range :"))
b=int(input("Enter the ending number of the range "))
n=int(input("Enter how many random numbers you want"))
number=[]
for i in range(n):
    number.append(random.randint(a,b))
print("The list of random numbers is :",number)