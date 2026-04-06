# example of how self and object are referring to same instance
class check:
    def __init__(self):
        print("Address of self = ",id(self))
# Inside __init__
# print("Address of self = ", id(self))
# self refers to the same object that was just created.
# id(self) gives the memory address (identity) of that object.


obj = check() # A new object (instance) of class check is created.
# Python internally does something like:
# Allocate memory for the object
# Call __init__(self) with that object
# 👉 That object is passed as self.

print("Address of class object = ",id(obj))
# id(obj) prints the same memory address.

# OUTPUT::
# Address of self =  140245678912
# Address of class object =  140245678912

# 🔹 Key idea
# self = the instance inside the class
# obj = the reference to that instance outside the class
# ✅ They point to the same memory location