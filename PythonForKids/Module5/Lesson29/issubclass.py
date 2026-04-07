class animals:
    pass
class dog(animals):
    pass
class cat(animals):
    pass
print("is dog subclss of animals",issubclass(dog,animals))
print("is cat  subclass of dog : ",issubclass(cat,dog))