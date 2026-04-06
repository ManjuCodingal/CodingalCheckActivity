import math

# Create class Circle
class Circle:
    
    # Constructor to initialize radius
    def __init__(self, radius):
        self.radius = radius
    
    # Method to calculate area
    def area(self):
        return math.pi * self.radius ** 2
    
    # Method to calculate perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# Take input from user
r = float(input("Enter the radius: "))

# Create object of Circle class
c = Circle(r)

# Display results
print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())