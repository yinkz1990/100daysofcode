#for qaudratic equation of these form ax^2 + bx +c=0
#import complex math module
import cmath
#using the integer and input text
a= int(input("a ="))
b= int(input("b = "))
c= int(input("c = "))
# to calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions 
x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)
print(d)
print(x1)
print(x2)




