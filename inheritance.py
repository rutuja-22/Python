#MRO method resolution order....always left to right
#in multiple inheritance by using super only first inherited class's init or method can be call
class A:
    def __init__(self):
        print("A init")

    def m1(self):
        print("Method A")

class B:
    def __init__(self):
        print("B init")
    
    def m2(self):
        print("Method B")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")

    def m3(self):
        print("Method C")  

a = C()
a.m1()
a.m2()
a.m3()