class dog:
    species='animal'
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=dog("Bruno ",10)
obj2=dog("Puppy",12)
print( obj1.name,"is a ",obj1.age,"years old dog")

print( obj2.name,"is a ",obj2.age,"years old dog")



