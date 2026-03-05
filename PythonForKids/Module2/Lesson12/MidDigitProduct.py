#Input a number 
num = int(input("Enter the number : "))
t = num # store the number in a temporary variable to find the length of the number
numLen = 0
#iterate the loop
while t>0: 
  numLen = numLen+1
  t = int(t/10) # Remove the last digit of the number

if numLen>=4: #condition 1: continue to find the middle digits if the number has 4 or more digits
  numLen = int(numLen/2) #find the middle position of the number
  chk = 0 # To check the position of the digit
  while num>0: #iterate loop
    rem = num%10 # find the last digit of the number
    if chk==numLen: #nested condition 1 . if the position of the digit is equal to the middle position, store it in midOne variable
      midOne = rem
    elif chk==(numLen-1): # nested condition 2 . if the position of the digit is one less than the middle position, store it in midTwo variable
      midTwo = rem
    num = int(num/10) # Remove the last digit of the number
    chk = chk+1 #increment the position of the digit
  prod = midOne*midTwo #product of middle digits
  #display the result
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
  print("\nIt's not a 4 or more than 4-digit number!")

# Outer while loop – Counting number of digits
# t = num  # temporary copy of the number
# numLen = 0

# while t > 0:
#     numLen = numLen + 1
#     t = int(t / 10)
# Purpose:
# To count how many digits the number has.
# How it works:
# t starts as a copy of the input number (num).
# numLen starts at 0.
# In each iteration:
# Increment numLen by 1 → counts one more digit.
# Remove the last digit from t using t = int(t / 10) (or t // 10 is cleaner).

# Example:
# Suppose num = 12345:

# Iteration	t	    numLen	Notes
# 1     	12345	1	    last digit removed → 1234
# 2     	1234	2	    last digit removed → 123
# 3     	123  	3	    last digit removed → 12
# 4     	12	    4	    last digit removed → 1
# 5     	1	    5	    last digit removed → 0

# After the loop ends: numLen = 5 → total number of digits.

# ✅ Outer loop only counts digits.

# Inner while loop – Finding the middle digits
# chk = 0  # position counter
# while num > 0:
#     rem = num % 10
#     if chk == numLen:
#         midOne = rem
#     elif chk == (numLen - 1):
#         midTwo = rem
#     num = int(num / 10)
#     chk = chk + 1
# Purpose:
# To extract the two middle digits of the number.
# Works from right to left (least significant digit first).
# How it works:
# chk keeps track of the current position of the digit, starting at 0 from the rightmost digit.
# rem = num % 10 → gives the last digit of num.

# if chk == numLen → store in midOne (first middle digit)
# elif chk == (numLen - 1) → store in midTwo (second middle digit)
# Remove last digit of num: num = int(num / 10)
# Increment chk by 1 → move left.

# Example:
# Suppose num = 123456:

# ⭐ Number of digits: 6 → numLen = 6 // 2 = 3
# ⭐ Goal: middle digits are 3 and 4 (from 123456).

# chk	num 	rem = num % 10	Action
# 0  	123456	6	            skip
# 1 	12345	5	            skip
# 2	    1234	4	            midTwo = 4
# 3	    123 	3	            midOne = 3
# 4	    12	    2	            skip
# 5 	1	    1	            skip

# After the loop: midOne = 3, midTwo = 4

# Product: 3 * 4 = 12 ✅

# Notes:
# The loop starts from the last digit and moves left.
# chk ensures we know the position of each digit relative to the right end.
# num becomes 0 after the loop ends → all digits have been processed.

# Summary
# Loop      	Purpose  	                                  Counts/Extracts	      
# Outer while	Count the number of digits (numLen)           Increments numLen	 
# Inner while	Find the two middle digits (midOne, midTwo)	  Uses chk to track position, extracts middle digits	 

# ✅ The outer loop just counts digits.
# ✅ The inner loop extracts the middle digits using position tracking.