 
start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

even_squares = []
odd_squares = []

print("Squares of numbers between", start, "and", end, ":")
 
for i in range(start, end + 1):
    square = i ** 2
    print(f"{i}^2 = {square}")
    
    # Check even or odd
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("\nEven Squares:", even_squares)
print("Odd Squares:", odd_squares)