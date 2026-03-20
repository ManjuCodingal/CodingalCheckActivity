# Write a program to understand how the value error exception works?
try:
    num=int(input("Enter your number ; ")) 
    print("The number is ",num)
except  ValueError as error :
    print("eception is ",error)

# try:
#     num=str(input("Enter your number ; ")) # str converts value into a string.Strings do not pose Value Error.
#     print("The number is ",num)
# except  ValueError as error :
#     print("eception is ",error)
   