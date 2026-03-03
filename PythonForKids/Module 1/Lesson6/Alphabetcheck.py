 # Method 1: Using .isalpha()
while True:
    user_input = input("Method 1 - Enter a single character: ")
    
    if len(user_input) == 1:#Checking lenght of input
        if user_input.isalpha():#use isaplha func
            print("The input is an alphabet (Method 1).")
        else:
            print("The input is not an alphabet (Method 1).")
        break#Loop breaks
    else:
        print("Invalid input! Enter only ONE character.")

print("\n--- Now using Method 2 ---\n")#Next line

# Method 2: Using comparison operators
while True:
    user_input = input("Method 2 - Enter a single character: ")
    
    if len(user_input) == 1:
        ch = user_input
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            print("The input is an alphabet (Method 2).")
        else:
            print("The input is not an alphabet (Mehtod 2).")
        break
    else:
        print("Invalid input. Enter only ONE character.")


