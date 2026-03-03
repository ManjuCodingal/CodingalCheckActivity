# Swap three numbers 

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

print("\nBefore Swapping:")
print("a =", a, "b =", b, "c =", c)

# Circular swapping using multiple assignment
a, b, c = b, c, a

print("\nAfter Swapping:")
print("a =", a, "b =", b, "c =", c)