class pair_elemants:
    def sum_num(self,nums,sum):
         

        for i in range(len(nums)): # i is the first number’s index. It goes from 0 to last index
            for j in range(i+1,len(nums)): # j is the second number’s index. It starts from i+1 to avoid repeating pairs and to ensure that we are always looking at pairs of different numbers.
                if nums[i]+nums[j]==sum: # checks if the sum of the two numbers at index i and j equals the target sum provided by the user. If it does, it means we have found a valid pair of numbers that add up to the target sum.
                    return i,j # If a valid pair is found, the function returns the indices of the two numbers as a tuple (i, j). This allows us to identify which two numbers in the list add up to the target sum.

value=int(input("enter a sum : "))
obj=pair_elemants() # creates an instance of the pair_elemants class, which allows us to call the sum_num method to find pairs of numbers that add up to the specified sum.
result=obj.sum_num((10,20,30,40,50,60,70),value) # calls the sum_num method of the pair_elemants class instance (obj) with a tuple of numbers (10, 20, 30, 40, 50, 60, 70) and the user-provided target sum (value). The method will search for pairs of numbers in the tuple that add up to the target sum and return their indices if found.
if result:
    print("index 1 is equal to",result[0],"index 2 is equal to ",result[1])
else:
    print("No pair found !!")