# Function to calculate circumference
def circumference(r):
    c = 2 * 3.14 * r
    return c

# Input from user
radius = float(input("Enter radius: "))

# Function call
result = circumference(radius)

print("Circumference of circle is:", result)