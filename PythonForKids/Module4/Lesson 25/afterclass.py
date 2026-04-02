# 1️. Take a number from the user and create a list of odd numbers under it
n = int(input("Enter a number: "))
odd_numbers = [i for i in range(n) if i % 2 != 0]
print("List of odd numbers:", odd_numbers)

# 2️. Create a list of fruits and capitalize the first letter of each
fruits = ["apple", "banana", "mango", "grapes"]
updated_fruits = [fruit.capitalize() for fruit in fruits]
print("Updated list of fruits:", updated_fruits)