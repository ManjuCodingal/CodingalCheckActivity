#  Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)

class pair_elemants:
    def sum(self,nums,sum):
        lookup={}

        for i ,j in enumerate(nums,1): # position j starts from 1 . by default if noting is given it will strat from 0.
            if sum-j in lookup:
                return (lookup[sum-j],i)
            lookup[j]=i

value=int(input("enter a sum : "))
obj=pair_elemants()
result=obj.sum((10,20,30,40,50,60,70),value)
print(result)
        