# Create a parent class Student with: name, roll number, A method display()

# Create a child class Marks that: Inherits from Student, Adds marks, Displays student details along with marks

# Create another child class Sports that:, Inherits from Student Adds sport name, Displays student details along with sport

# Create at least two objects for each child class and display their details.

# Add a new method in Marks to:

# Print "Pass" if marks ≥ 40, otherwise "Fail".

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


class Marks(Student):
    def __init__(self, name, roll_no, marks):
        super().__init__(name, roll_no)
        self.marks = marks

    def display(self):
        super().display()
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


class Sports(Student):
    def __init__(self, name, roll_no, sport):
        super().__init__(name, roll_no)
        self.sport = sport

    def display(self):
        super().display()
        print("Sport:", self.sport)


 
m1 = Marks("Rahul", 1, 75)
m2 = Marks("Aman", 2, 35)

 
s1 = Sports("Priya", 3, "Cricket")
s2 = Sports("Neha", 4, "Football")



print("---- Marks Students ----")
m1.display()
m1.result()

print()
m2.display()
m2.result()

print("\n---- Sports Students ----")
s1.display()

print()
s2.display()
# -----------------------------------------------------------Afterclass-----------

class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()   # get fare from Vehicle
        maintenance = 0.10 * base_fare
        return base_fare + maintenance


# Create Bus object
school_bus = Bus("School Bus", 80, 12, 50)

print("Total Bus Fare:", school_bus.fare())