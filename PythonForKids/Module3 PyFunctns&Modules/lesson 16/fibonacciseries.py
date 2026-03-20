def fibonacci(n):
    """
    Fibonacci Series:
    A sequence of numbers where each number is the sum of the two
    preceding numbers. The series usually starts with 0 and 1.

    Formula:
    F(n) = F(n-1) + F(n-2)

    Example:
    0, 1, 1, 2, 3, 5, 8, 13 ...
    """

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Enter the number of terms: "))

print("Fibonacci Sequence:")

for i in range(num):
    print(fibonacci(i))