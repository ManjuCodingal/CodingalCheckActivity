# Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
num_1=int(input("Enter first number : "))
num_2=int(input("Enter second number :"))
print("Choose your operation\na.add ")
# print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
operation=input("Enter the option : ")
if operation=="a":
    ad=add(num_1,num_2) 
    print(ad)
elif operation=="b":
    sub=subtract(num_1,num_2)
    print(sub)
elif operation=="c":
    mul=multiply(num_1,num_2)
    print(mul)
elif operation=="d":
    div=divide(num_1,num_2)
    print(div)
else:
    print("Invalid input! Pls chose from a, b, c,d")
