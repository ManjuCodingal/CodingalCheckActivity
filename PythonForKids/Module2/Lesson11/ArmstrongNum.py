# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit (ie Armstrong number)

# Eg of 153. 1^3+5^3+3^3=1+125+27=153
temp = num
while temp > 0:
   digit = temp % 10 # % 10 (remainder) gives the last digit. % is the modulus operator
   sum += digit ** 3
   temp //= 10 # // 10 (floor division) removes the last digit

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")