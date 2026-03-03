#Write a program to illustrate the use of 'is' identity operator.
#is , is not
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
list3=[16,7,8,9]
print("list1 is list 2",list1 is list2) #False if list1==list2 , it will be true.here they are diff onj in memory so list1 is list 2 will be false
print("list1 is not  list2",list1  is not  list2)#true
print("list1 is list3",list1 is list3) #false

x=5
if (type(x)is int) :
    print("True")
y=5.89
if (type(y) is float) :
    print("True")
z=20
if (x is z) :
    print("True")
else:
    print("False")
if (x is not y):
    print("True")
else :
    print("False")