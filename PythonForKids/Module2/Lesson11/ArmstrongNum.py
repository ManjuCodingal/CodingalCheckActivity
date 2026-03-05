# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit (ie Armstrong number)

# Eg of 153. 1^3+5^3+3^3=1+125+27=153
temp = num
while temp > 0:
   digit = temp % 10 # % 10 (remainder) gives the last digit. % is the modulus operator
   sum += digit ** 3 # Gives for 3 digits. For 4 digits, it will be digit ** 4
   temp //= 10 # // 10 (floor division) removes the last digit

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# BETTER WAY::
# Generalised code for n-digit Armstrong number
# number = int(input("Input your number: "))
 
# # Calculate number of digits
# digits = len(str(number))
 
# # Initialize result variable
# resultNumber = 0
 
# # find the sum of the a^digits of each digit
# temp = number
# while temp > 0:
#    digit = temp % 10
#    resultNumber += digit ** digits
#    temp //= 10
 
# # display the result
# if number == resultNumber:
#    print(number,"is an Armstrong number")
# else:
#    print(number, "is not an Armstrong number") 