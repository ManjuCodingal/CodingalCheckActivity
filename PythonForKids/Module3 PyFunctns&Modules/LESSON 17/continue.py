# Write a program to display 1 to 10 numbers in reverse order and skip the number 5.
for i in range(10,0,-1): # Range starting from 10 to 0 and decrseing i each time by -1
     
    if i==5: 
        continue
    print(i)
