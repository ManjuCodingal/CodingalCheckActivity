correctPassword=12345
for i in range(3):
    password=int(input("Enter your password : "))
    if password==correctPassword:
        print("login succesful!")
        break
    else:
        print("Password is incorrect ,try again")