# Print heading
print("Mirrored Right Triangle Pattern")

# Take input from user
n = int(input("Enter number of rows: "))

# Outer loop for rows
for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    for j in range(i):
        print("*", end="")

    # Move to next line
    print()