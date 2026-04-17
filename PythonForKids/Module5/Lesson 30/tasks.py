# Create a Rectangle class that allows you to set the dimensions of the rectangle but prevents direct access to the length and width. Use setter methods to change length, and create methods to compute the area and perimeter
class Rectangle:
    def __init__(self, length, width):
        # Private attributes
        self.__length = length
        self.__width = width

    # Setter for length
    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print("Length must be positive.")

    # Setter for width
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be positive.")

    # Method to calculate area
    def area(self):
        return self.__length * self.__width

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.__length + self.__width)

    # Optional: method to get dimensions safely
    def get_dimensions(self):
        return (self.__length, self.__width)

# Example usage
rect = Rectangle(5, 3)
print("Area:", rect.area())            # 15
print("Perimeter:", rect.perimeter())  # 16

rect.set_length(10)
rect.set_width(4)
print("Updated Area:", rect.area())    # 40
print("Updated Perimeter:", rect.perimeter())  # 28