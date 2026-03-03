# Taking input from user  
word = input("Enter the word  : ")#Conratulations

# 1. Make first letter uppercase and rest lowercase (Capitalize)
capitalized_word = word.capitalize()
print("Capitalized word:", capitalized_word)

# 2. Convert entire word to uppercase
upper_word = word.upper()
print("Uppercase word:", upper_word)

# 3. Convert entire word to lowercase
lower_word = word.lower()
print("Lowercase word:", lower_word)

# 4. Slice the word (example: first 5 letters)
slice_word = word[:5]
print("First 5 letters:", slice_word)

# 5. Reverse the word using slicing
reverse_word = word[::-1]
print("Reversed word:", reverse_word)
