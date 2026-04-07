# Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def pnt(self):
#         return (self.x,self.y)
# obj=Point(3,6)
# print("Coordinates of the point are : ",obj.pnt())

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __pnt__(self): # This is a special method.
        return (self.x,self.y)
obj=Point(3,6)
print("Coordinates of the point are : ",obj.__pnt__())

