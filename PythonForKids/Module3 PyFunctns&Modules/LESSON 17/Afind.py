# Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.”
a=input("Enter a word : ").lower()
for i in a:
    if i=='a':
        print("A is found")
        break 
    else:
        print("A is not found")