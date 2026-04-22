# Using math module
# Caluculation of radius and circumference 
import math
def circle(radius):
    area=math.pi*math.pow(radius,2)
    circumference=2*math.pi*radius
    return area,circumference
r=float(input("Enter radius of circle whose circumference and area is to be calculated :"))
a,c=circle(r)
print("The area of circle is:",a,"The circumference is:",c,".")

#calculation of factorial of a number
n=int(input("Enter the number whose factorial is to be calculated"))
fact=math.factorial(n)
print("The factorial of :",n,"is:",fact)
