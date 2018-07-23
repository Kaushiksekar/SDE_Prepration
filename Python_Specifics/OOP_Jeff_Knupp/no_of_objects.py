class A:
    no_of_objects = 0

    def __init__(self):
        A.no_of_objects += 1

    @classmethod
    def get_no_of_objects(cls):
        return cls.no_of_objects

a = A()
print(A.get_no_of_objects())
b = A()
print(A.get_no_of_objects())
