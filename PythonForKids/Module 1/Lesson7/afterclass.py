# ASCII Character Analyzer Program

char = input("Enter a single character: ")

# Validate input length
if len(char) != 1:
    print("Error: Please enter exactly ONE character.")
else:
    # Validate type using type() and is
    if type(char) is str:
        
        # Get ASCII value
        ascii_value = ord(char)
        print("ASCII Value:", ascii_value)

        # Categorize character
        if 'A' <= char <= 'Z':
            print("Character Type: Uppercase Letter")
        elif 'a' <= char <= 'z':
            print("Character Type: Lowercase Letter")
        elif '0' <= char <= '9':
            print("Character Type: Digit")
        else:
            print("Character Type: Special Character")