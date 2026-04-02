# Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple

tuple_1=("Hello",True,2.56,8)
print("Tuple with mixed datataypes",tuple_1)

tuple_2=(2,3,4,5)
print("Tuple with integer datatype : ",tuple_2)

tuple_3=(11,12,13,14)
print("Tuple by adding 9 to each term of previous tuple.",tuple_3)

tuple_4=tuple_3+(9,)
print(tuple_4)

tuple_5=(1,1,1,3,4,5,5,4,6)
print(tuple_5.count(1))

print(tuple_5[2:7])
 

