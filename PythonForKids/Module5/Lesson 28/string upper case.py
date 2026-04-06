#  Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.

class IOSstring:
    def __init__(self):
        self.str1=""
    def string_get(self):
        self.str1=input("Enter ny string : ")
    def print_string(self):
        print(self.str1.upper())

ob=IOSstring()
ob.string_get()
ob.print_string()