# Check number is even and greater than 10
number=int()

if number % 2 == 0 and number > 10:
    print("Even and greater than 10")
else:
    print("Condition not satisfied")



if number % 2 == 0:
    if number > 10:
        print("Even and greater than 10")
    else:
        print("Even but not greater than 10")
else:
    print("Not even")
