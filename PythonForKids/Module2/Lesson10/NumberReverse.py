# Write a program to print the numbers in reverse order beginning from the number entered by the user.
num=int(input("Enter your number : "))

for i in range(num,0,-1): # range(start,stop,stepsize)
    print(i)