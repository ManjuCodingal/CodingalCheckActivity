# Write a program to understand the different functions of the math module.
import math

a=math.ceil(0.24)
b=math.floor(20.98)
print("ceiling of 0.24 is",a,"floor of 20.98 is ",b)
x=12
y=-1
c=math.copysign(x,y)
print("copysign of x=12 and y=-1 is",c)
print("absolute value of -19 is ",math.fabs(-19))