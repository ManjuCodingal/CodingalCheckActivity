# Program to check if light clothes are suitable

temperature = float(input("Enter the current temperature in °C: "))

if temperature >=25:
    print("It is warm. You can wear light and soft clothes.")
elif temperature >= 18 and temperature < 25:
    print("The weather is moderate. You may wear light clothes with a thin layer.")
else:
    print("It is cold. Wear a jacket or pullover to avoid getting sick.")
#Program to print family size

members = int(input("Enter total NUMBER of members in your family."))

if members <=4 :
    print("Your family is nuclear family")
else :
    print("Your family ia joint family.")

