# Define the Reverse class
class Reverse:
    def __init__(self, s=""):
        self.s = s  # initialize string, default empty

    def get_reversed(self):
        """Return the reversed string"""
        return self.s[::-1]  # slicing to reverse


# Take input from user
user_input = input("Enter a word: ")

# Create Reverse object with user input
r = Reverse(user_input)

# Print the reversed string
print("Reversed string:", r.get_reversed())