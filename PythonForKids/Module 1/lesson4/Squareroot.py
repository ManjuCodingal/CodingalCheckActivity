import math

# Take input from user
a = float(input("Enter a number: "))

# Method 1 
print("\nMethod 1: Using math.sqrt()")
result1 = math.sqrt(a)
print("Square root is:", result1)

# Method 2 
print("\nMethod 2: Using exponent (** 0.5)")
result2 = a ** 0.5
print("Square root is:", result2)
