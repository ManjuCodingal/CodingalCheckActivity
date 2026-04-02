# Write a program where the value of i begins from 1 and goes to 10. When the value of i becomes 5, force the interpreter to exit the program.

# for i in range(1,11):
#     print("i=",i)
#     if i==5:
#         print("i has reached 5!")
#         exit()

import sys
for i in range(1,11):
    print("i=",i)
    if i==5:
        print("i has reached 5!")
        sys.exit()

for i in range(1,11):
    print("i=",i)
    if i==5:
        print("i has reached 5!")
        break                            # Break will just BREAK THE LOOP.exit() exits the WHOLE PROGRAMME,the rest of the code in that file wont get executed
print("this is the line outside for loop")