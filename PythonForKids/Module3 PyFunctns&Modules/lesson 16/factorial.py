# Write a program to find the factorial using recursive function
def factorial(num):
    '''This function defines the factorial of a number using recursion.Recursion is function calling itself. '''
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("Enter your number : "))
print(factorial.__doc__)
print("factorial is : ",factorial(num))