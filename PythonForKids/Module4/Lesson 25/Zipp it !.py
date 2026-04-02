# Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary.

list_1=[1,2,3]
list_2=[2,4,6]

list_3=list(zip(list_1,list_2))
print("zipped list is : ",list_3)

print("zipping reversed list 2 with list 1")
for x,y in zip(list_1,list_2[::-1]):
    print(x,y)

new_dict={x:y for x,y in zip(list_1,list_2)}
print(new_dict)

results={}
for x,y in zip(list_1,list_2):
    results[x]=y # Indexing is used.
print(results)