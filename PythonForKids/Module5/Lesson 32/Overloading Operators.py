# Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.
class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other): # lt ----less than
        if self.a<other.a:
            return "object 1 is lesser as compared to object 2."
        else:
            return "object 1 is greater as compared to object 2 ."
    def __eq__(self,other): # eq----equal to # ne ----- not equal to
        if self.a==other.a:
            return "both the objects are equal !"
        else:
            return"both obj are not equal"
obj1=A(3)
obj2=A(4)
print(obj1.a)
print(obj2.a)
print(obj1 < obj2)
obj3=A(5)
obj4=A(5)
print(obj3.a)
print(obj4.a)
print(obj3==obj4)
obj5=A(9)
obj6=A(3)
print(obj5 == obj6)
print(obj5<obj6)