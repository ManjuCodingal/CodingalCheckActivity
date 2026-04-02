# Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.

arr=[1,3,5,3,7,9,3]

count_3=arr.count(3)

reversed_array=arr[::-1]

print("Original array : ",arr)
print("Count of 3 : ",count_3)
print("Reversed array : ",reversed_array)

# ------------------------------------------------------------------

import array as arr

array_num=arr.array('i',[1,3,5,3,7,9,3])

count_3=array_num.count(3)

reversed_array=array_num[::-1] 
array_num.reverse()
print('Reversed array is :',array_num)

print("Original array : ",array_num)
print("Count of 3 : ",count_3)
print("Reversed array : ",reversed_array)
