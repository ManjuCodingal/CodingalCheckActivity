string = input("Please enter your own String : ")

string2 = ('')
#loop for printing in reverse 
for i in string:
    string2 = i + string2
    
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)

# Example:
# string = "hello"
# Iteration 1:
# i = "h"
# string2 = "h" + "" = "h"
# Iteration 2:
# i = "e"
# string2 = "e" + "h" = "eh"
# Iteration 3:
# i = "l"
# string2 = "l" + "eh" = "leh"
# Iteration 4:
# i = "l"
# string2 = "l" + "leh" = "lleh"
# Iteration 5:
# i = "o"
# string2 = "o" + "lleh" = "olleh"

# Why This Reverses the String?

# Because you are adding each new character in front of the previous result:
# string2 = i + string2
# Instead of:
# string2 = string2 + i   ❌ (this would keep same order)

# Easier Way (Python Shortcut)
# Python has a built-in slicing trick:
# string2 = string[::-1]