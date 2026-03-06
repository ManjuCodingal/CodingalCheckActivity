# Output: Diamond Pattern of Numbers:
# enter the number of rows: 4 (Even number of rows)
#  1
# 123
#  1

# enter the number of rows: 5 (Odd number of rows)
#   1
#  123
# 12345
#  123
#   1

#take input from user
rowSize = int(input("enter the number of rows: "))
if rowSize%2==0: #conditions to check whether the number of rows is even or odd
  halfDiamRow = int(rowSize/2) # if even then half of the number of rows will be the number of rows in upper part of diamond. Eg. if rowSize is 4 then halfDiamRow will be 2 because 4/2 is 2.

else:
  halfDiamRow = int(rowSize/2)+1 # if odd then half of the number of rows + 1 will be the number of rows in upper part of diamond, if decimal value is there then it will be converted to integer by int() function and 1 will be added to it. Eg. if rowSize is 5 then halfDiamRow will be 3 because 5/2 is 2.5 and int(2.5) is 2 and 1 will be added to it to make it 3.


#loop for upper part of diamond  
space = halfDiamRow-1 # number of spaces in the first row will be one less than the number of rows in upper part of diamond. Eg. if halfDiamRow is 3 then space will be 2 because 3-1 is 2. Space is used to print spaces before the numbers in each row to make the pattern look like a diamond.

# Main for loop, purpose: to get number of rows
for i in range(1, halfDiamRow+1):  
  # Inner for loop, purpose: to get columns
  # Inner for loop 1
  for j in range(1, space+1): # 1st for loop purpose: to give spaces   
    print(end=" ")
  space = space-1
  num = 1
  # Inner for loop 2 purpose: to print numbers in each row
  for j in range(2*i-1):
    print(end=str(num))
  #incerementing number at each column
    num = num+1
  print()

space = 1 # NOTE:IMP. space is updated to 1 because in the first row of lower part of diamond there will be one space before the numbers.  

#loop for lower part of diamond

# outer for loop purpose: to get number of rows
for i in range(1, halfDiamRow): 
  # inner for loop is to get columns
  for j in range(1, space+1):  # inner for loop 1 purpose: to give spaces
    print(end=" ")
  space = space+1
  num = 1
  for j in range(1, 2*(halfDiamRow-i)): # inner for loop 2 purpose: to print numbers
    print(end=str(num)) #display result
  #incerementing number at each column
    num = num+1
  print()

#✅ EXAMPLE 1: Odd rowSize = 5
# Example upper half 
# i	spaces	numbers
# 1	 2    	1
# 2	 1	    123
# 3  0    	12345

# Output:
#   1
#  123
# 12345

# Example lower half  
# i	spaces	numbers
# 1	 1	    123
# 2	 2     	1

# Output:
#  123
#   1

#✅ EXAMPLE 2: Even rowSize = 4
#  1    upper half
# 123   upper half
#  1    lower half