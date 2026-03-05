# Program to count number of digits using while loop

num = int(input("Enter a number: "))

# If number is 0, it has 1 digit
if num == 0:
    count = 1
else:
    count = 0
    num = abs(num)   # To handle negative numbers
    
    while num > 0:
        num = num // 10   # Remove last digit
        count += 1        # Increase count

print("Number of digits:", count)

# Or

num = int(input("Enter a number: "))
num = abs(num)

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10
        count += 1

print("Number of digits:", count)