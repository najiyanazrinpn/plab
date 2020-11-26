from math import *
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
det = (b*b)-(4*a*c)
s1 = (-b+sqrt(det))/(2*a)
s2 = (-b-sqrt(det))/(2*a)
print("The roots are ",s1,", ",s2)
