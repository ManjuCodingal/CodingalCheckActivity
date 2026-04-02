# Import the 'random' module to generate random numbers and choices
import random

# Import the 'string' module to access predefined sets of characters
import string

# Define lowercase letters (a-z) using string module
lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

# Define uppercase letters (A-Z) using string module
uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Define digits (0-9) using string module
numbers = string.digits  # '0123456789'

# Combine all characters (lowercase + uppercase + digits) into one string
all_chars = lowercase + uppercase + numbers

# Define the desired password length
password_length = 12  # You can change this to make longer or shorter passwords

# Generate a random password by picking characters randomly from all_chars
# The 'for _ in range(password_length)' repeats the process 'password_length' times
# ''.join(...) converts the list of characters into a single string
password = ''.join(random.choice(all_chars) for _ in range(password_length))

# Convert the password string into a list of characters to shuffle them
password_list = list(password)

# Shuffle the list of characters to make the password more unpredictable
random.shuffle(password_list)

# Convert the shuffled list back into a single string
password = ''.join(password_list)

# Print the final random password
print("Random Password:", password)