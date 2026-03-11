def pnz_check(num):
    if num>0:
        print("The number is positive.")
    elif num<0:
        print("The number is negative.")
    else:
        print("The number is 0.")
num=int(input("Entre your number : "))
pnz_check( num )