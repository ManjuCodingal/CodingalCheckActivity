# Function to calculate average
def average(a, b, c):
    avg = (a + b + c) / 3
    return avg

# Taking input
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

# Function call
result = average(n1, n2, n3)

print("Average is:", result)