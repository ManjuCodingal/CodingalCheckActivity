#  Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well

class parrot:
    species="birds"

    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=parrot("Macow",14)
obj2=parrot("Red eyed ",12)

print("object 1 is of species  ",obj1.species)
print("Object 2 is of species ",obj2.species)
print("Obj 1 name is ",obj1.name,"an age is ",obj1.age)
print("Obj 2 name is ",obj2.name,"an age is ",obj2.age)
