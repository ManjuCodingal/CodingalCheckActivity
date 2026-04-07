#  Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.

class Bird:
    def __init__(self):
        print("base class is made")

    def species(self):
        print("bird")
    def swim(self):
        print("it will swim")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("class penguin is ready !")
    def species(self):
        print("bird")
    def fly(self):
        print("it will fly")
obj=Penguin()
obj.species()
obj.swim()
obj.fly()

    