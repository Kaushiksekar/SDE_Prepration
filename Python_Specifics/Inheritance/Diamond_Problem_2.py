class A:
    def m(self):
        print("m of A")

class B(A):
    pass

class C(A):
    def m(self):
        print("m of C")

class D(B,C):
    pass

x = D()
x.m() # prints m of C as B has nothing
# In python 2, it would print m of A
# This order of browsing through base classes is called Method Resolution
# Order(MRO)
