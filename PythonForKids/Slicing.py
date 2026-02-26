# Str = "string"

# print(Str[3:])

# print(Str[0:1])

# print(Str[-1]) last element
# print(Str[-2]) Second last element
# print(Str[0:6:3])

#input a word
text = str(input("Enter a string: "))

# Reverse String 
# using step value as -1 to iterate in reverse
revText = text[::-1] 
text = revText

print("Reverse of Given String is:")
print(text)