# Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.

List=[10,20,30,40,15]
print("Intial list is :",List)

sum=0

for i in List:
    sum=sum+i
avg=sum/len(List)

print("Sum is ",sum)
print("Avegare is ",avg)

List.sort()

print("Smallest number is ",List[0])
print("Largest number is ",List[-1])