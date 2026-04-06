#  Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!

class employee:
    def __init__(self):
        print("named employee class created" )
    def __del__(self):
        print("Destructor created")

def Create():
    print("Making object!")
    obj=employee()
    print("object is ceated")
    return obj

obj=Create()