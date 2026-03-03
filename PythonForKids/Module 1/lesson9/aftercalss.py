# Program to check enrollment eligibility based on age

age = int(input("Enter your age: "))

if 10 <= age <= 20:
    print("You can enroll in the class.")
elif age > 20:
    print("You cannot enroll. Age is above 20.")
else:
    print("You cannot enroll. Age is below 10.")