# WAP to calculate sum of first n natural  numbers .
def naturalsum(num):
    if num==1:
        return 1
    else :
        return num+naturalsum(num-1)
num=int(input("Enter your number : "))
print("The sum of natural numbers till",num,"is",naturalsum(num))
