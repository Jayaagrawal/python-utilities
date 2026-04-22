#Demonstrates the difference between three math operations 'ceil','floor' and 'trunc
import math
def rounding(num,choice):
    if choice==1:
        return math.ceil(num)
    elif choice==2:
        return math.floor(num)
    elif choice==3:
        return math.trunc(num)
    else:
        return"Invalid choice"
print("Rounding Utility")
c=int(input("Enter your choice:1)Ceil of number  2)floor of number  3)trunc of number  :"))

n=float(input("Enter any number:"))
result=rounding(n,c)
print("The result of rounding is :",result)
