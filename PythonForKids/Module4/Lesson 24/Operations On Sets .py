# Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

my_set={1,2,3}
print("Set with integers : ",my_set)

my_set={1,'Hello',1.23}
print("Set with mixed datatypes : ",my_set)

my_set={1,2,3,4,3,2,4}
print("Set without duplicates : ",my_set) # A set cannot have duplicates

my_set=set([1,2,3,2]) # set method is used to convert list to set .
print("Set from list : ",my_set)

my_set=set([0,1,3,4,5])
my_set.pop() # Pop will rmeove 1st item 
print("Set after removing 1st item is : ",my_set)