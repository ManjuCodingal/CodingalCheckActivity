#take two input from user
lower = int(input("enter a lower range: "))
upper = int(input("enter a upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")
#iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0: # if the number is divisible by any number between 2 and num-1, then it is not prime. % is the modulus operator which gives the remainder of the division
               break
       else:
           print(num)