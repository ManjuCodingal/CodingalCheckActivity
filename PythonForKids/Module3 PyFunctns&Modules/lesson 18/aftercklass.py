try:
    age = int(input("Enter your age: "))

    if age % 2 == 0:
        print("Age is Even")

    else:
        print("Age is Odd")

except ValueError:
    print("Value Error! Please enter a valid integer age.")