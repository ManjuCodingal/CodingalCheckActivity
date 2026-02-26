# Give a python prm to check whether a given character is alphabet or not?

# Using isalpha()-------------------------
ch = input("Enter a character: ")

if ch.isalpha():
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")

# isalpha() returns True if the character is a letter (a–z or A–Z).
# Otherwise, it returns False.

# Using ASCII Range Check-------------------------
ch = input("Enter a character: ")

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")
# ----------------------------------------to make sure the user enters only one character
ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")

# Using if, elif, and logical operators ---------------------
ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter a single character.")
elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")

# Using not--------------------- 
ch = input("Enter a character: ")

if len(ch) == 1 and not ((ch < 'A') or (ch > 'z') or (ch > 'Z' and ch < 'a')):
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")