# Create a parent class Student with:
# name
# roll number
# A method display()
# Create a child class Marks that:
# Inherits from Student
# Adds marks
# Displays student details along with marks
# Create another child class Sports that:
# Inherits from Student
# Adds sport name
# Displays student details along with sport
# Create at least two objects for each child class and display their details.
# Add a new method in Marks to:
# Print "Pass" if marks ≥ 40, otherwise "Fail".

# Eg of 1 parent class and 2 child classes with inheritance and method overriding


# Parent class
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)


# Child class 1
class Marks(Student):
    def __init__(self, name, roll, marks):
        self.marks = marks
        Student.__init__(self, name, roll)

    def show(self):
        self.display()
        print("Marks:", self.marks)


# Child class 2
class Sports(Student):
    def __init__(self, name, roll, sport):
        self.sport = sport
        Student.__init__(self, name, roll)

    def show(self):
        self.display()
        print("Sport:", self.sport)


# Objects
m = Marks("Anil", 1, 85)
s = Sports("Ravi", 2, "Football")

m.show()
print("-----")
s.show()