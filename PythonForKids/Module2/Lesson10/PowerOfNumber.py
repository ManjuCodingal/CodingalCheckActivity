# Method 1: Equation method
# Analysis: Time complexity is O(log n) where n is the power.
# Space complexity is O(1) for iterative version and O(log n) for recursive version due to call stack.
base = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

result = base ** power

print("Result =", result)

# Method 2: For Loop method
# Analysis: Time complexity is O(n) where n is the power, as it requires n multiplications. Eg.If power = 1000 → 1000 multiplications
# Space complexity is O(1) since we only use a constant amount of space for the result variable. Because only one variable (result) is used.
base = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

result = 1

for i in range(power):
    result = result * base

print("Result =", result)

# Here, Method 1 (Equation method) is fastest. In general, O(log n) is faster than O(n) (especially when n becomes large). For very small numbers, we might not notice much difference. But for large numbers, O(log n) is MUCH faster.