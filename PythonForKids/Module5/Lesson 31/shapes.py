#  use polymorphism to implement the shapes classes with same mthod and different output
class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        print("rea of square is",self.side**2)
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area (self):
        print("Area of circle is ",self.radius**2*3.14)
obj1=Square(12)
obj2=Circle(12)
for i in (obj1,obj2):
    i.area()

# ----------------m2---------------------Using abstraction. for circle and for square
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of square is", self.side ** 2)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of circle is", self.radius ** 2 * 3.14)


obj1 = Square(12)
obj2 = Circle(12)

for i in (obj1, obj2):
    i.area()
     
        