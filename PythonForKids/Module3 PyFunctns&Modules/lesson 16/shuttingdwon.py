import os

def shutdown():

    answer = input("Do you want to shutdown the computer? (yes/no): ")

    if answer == "yes":
        print("Shutting down...")
        os.system("shutdown /s /t 10")

    elif answer == "no":
        print("Abort shutdown")

    else:
        print("Sorry")


shutdown()