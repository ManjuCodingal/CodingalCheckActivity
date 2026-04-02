# To check whether user_input is in set or not
set = {10, 20, 30}
user_input=int(input("Enter any number ; "))
if user_input in set:
    print("Your input in set.")
else:
    print("Your input not in set")

# -------------------------------------------------------------------------------

setA1={'blue','green'}
setA2={'green','yellow'}
setB1={1,2,3,4,5}
setB2={1,5,6,7,8,9}
print("Symmeric diff of seta1 and set a2 is : ",setA1^setA2)
print("Symmeric diff of setb1 and set b2 is : ",setB1^setB2)