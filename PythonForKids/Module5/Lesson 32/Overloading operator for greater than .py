class A:

    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if self.a > other.a:
            return True
        else:
            return False


obj1 = A(10)
obj2 = A(5)

if obj1 > obj2:
    print("obj1 is greater than obj2")
else:
    print("obj2 is greater or equal to obj1")