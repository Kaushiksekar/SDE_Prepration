class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")

class C(A):
    def m(self):
        print("m of C called")

class D(B, C):
    pass

x = D()
x.m()# will print B's m because B is the first class in D inheritance
# if order changed as C, B C's m would be printed
