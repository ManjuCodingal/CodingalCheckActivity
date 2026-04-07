# Create a Rectangle class that allows you to set the dimensions of the rectangle but prevents direct access to the length and width. Use setter methods to change length, and create methods to compute the area and perimeter. 
# Python implementation of the Rectangle class with encapsulation. This class allows you to set the dimensions (length and width) using setter methods, and provides methods to compute the area and perimeter. The length and width are private variables, and direct access to them is prevented.

class Rectangle:
    def __init__(self, length=0, width=0):
        # Initialize private variables
        self.__length = length
        self.__width = width

    # Setter method for length
    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print("Length must be positive.")

    # Setter method for width
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be positive.")

    # Getter method for length
    def get_length(self):
        return self.__length

    # Getter method for width
    def get_width(self):
        return self.__width

    # Method to calculate the area of the rectangle
    def area(self):
        return self.__length * self.__width

    # Method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.__length + self.__width)

    # Method to display the rectangle's details
    def display(self):
        print(f"Rectangle dimensions: {self.__length} x {self.__width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

# Example usage
rect = Rectangle()  # Create a Rectangle object with default values

# Set dimensions using setter methods
rect.set_length(5)
rect.set_width(3)

# Display rectangle's details
rect.display()

# Trying to set invalid dimensions
rect.set_length(-2)  # Invalid length (will show an error message)
rect.set_width(-4)   # Invalid width (will show an error message)

# Display updated details
rect.display()

# -------------------------------------------------------------
# Explanation:
# Private Variables:
# __length and __width are private variables, meaning they can't be accessed directly outside the class.
# Setter Methods:
# set_length() and set_width() are used to set the values for the private variables. They include validation to ensure that the values are positive. If a non-positive value is passed, an error message is displayed.
# Getter Methods:
# get_length() and get_width() return the current values of the private variables. These methods are not strictly necessary for this task but are included for completeness.
# Area and Perimeter:
# area() calculates the area of the rectangle using the formula length * width.
# perimeter() calculates the perimeter using the formula 2 * (length + width).
# Display Method:
# display() shows the rectangle's dimensions, area, and perimeter in a readable format.
# Output:
# Rectangle dimensions: 5 x 3
# Area: 15
# Perimeter: 16
# Length must be positive.
# Width must be positive.
# Rectangle dimensions: 5 x 3
# Area: 15
# Perimeter: 16

# In the above code:

# The Rectangle object is created with default dimensions 0 x 0, and then we set the dimensions using the setter methods (set_length and set_width).
# The display() method shows the calculated area and perimeter.
# Invalid attempts to set negative dimensions are caught by the setter methods, which print error messages without modifying the attributes.

# This is an example of encapsulation in action—ensuring that the internal state of the object (the length and width) is protected from invalid changes, and only allowed through controlled setter methods.