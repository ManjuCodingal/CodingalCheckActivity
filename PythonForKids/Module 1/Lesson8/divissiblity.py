#Write to check a number is divisible by another number

# numerator=int(input("Enter numerator :"))

# denominator=int(input("Enter your denominator : "))

# if denominator==0:

# print("Indefinite !not possible to divide..")

# elif numerator%denominator==0 :

# print("The numerator is divisible by denominator")

# else :

# print("The numerator is not divisible by denominator.")
numerator=int(input("Enter numerator :"))
denominator=int(input("Enter your denominator : "))

if denominator == 0:
    print("Indefinite !not possible to divide..")
else:
    a=numerator % denominator
    if a == 0 :
        print(f"The numerator{numerator} is didvsible by denominator{denominator}.")
    else:
        print(f"numerator{numerator} not div by denominator{denominator}.")
    