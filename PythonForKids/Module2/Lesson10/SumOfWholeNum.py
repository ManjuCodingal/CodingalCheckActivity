#Write a program to calculate the sum of whole numbers.
num=int(input("Enter the number till where you want to find the sum. : "))
sum=0
# for i in range(10):#here loop starts with i=0, ends with 10 , stepsize will be 1
#     print(i)

# for i in range(2,10):#here loop starts with i=2, ends with 10 , stepsize will be 1
#     print(i)#loop starts with i=2 

# for i in range(0,10,2):#here loop starts with i=0, ends with 10 , stepsize will be 2
#     print(i)

for i in range(1,num+1):
    sum=sum+i
    print("Sum = ",sum)
#print("Sum= ",sum)