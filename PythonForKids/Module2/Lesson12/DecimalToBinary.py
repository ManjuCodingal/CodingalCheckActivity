# Take input from the user
decimal = int(input("Enter a decimal number: "))

if decimal == 0:
    print("Binary: 0")
else:
    binary = ""
    n = decimal  # store original number

    while n > 0:
        remainder = n % 2       # get remainder (0 or 1)
        binary = str(remainder) + binary  # add it to the front
        n = n // 2              # divide n by 2

    print(f"Decimal {decimal} in binary is: {binary}")