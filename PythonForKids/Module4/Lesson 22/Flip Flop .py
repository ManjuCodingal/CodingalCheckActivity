# Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
tuple_1=(1,2,3,3,2,1)
def pallindrome(tuple_1):
    lenght=len(tuple_1)
    for i in range(lenght//2):
        if tuple_1 [i]!=tuple_1[lenght-i-1]:
            return False
         
    return True
# print("The tuple is ",pallindrome(tuple_1))
result=pallindrome(tuple_1)
# if result==True :
if result:
    print("Your tuple  is pallindrome!")
else:
    print("Your tuple is not a pallindrome.")

        
        