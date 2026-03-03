weight=float(input("Enter your weight in KILOGRAM"))
height=float(input("Enter your height in METER"))
BMI=weight/height**2
# BMI=weight/(height/100)**2  For height in cm
print("The BMI is ",BMI)
if BMI<=18.4 :
    print("You are underweight.")
elif BMI<=24.9 :
    print("You are healthy")
elif BMI<=29.9 :
    print("You are overweight.")
elif BMI<=34.9 :
    print("You are severely overweight.")
elif BMI<=39.9:
    print("You are obese.")
else :
    print('You are severely obese.')
