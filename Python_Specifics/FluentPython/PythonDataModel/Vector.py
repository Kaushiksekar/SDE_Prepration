from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, object):
        x = self.x + object.x
        y = self.y + object.y
        return Vector(x, y)

    def __mul__(self, num):
        return Vector(self.x * num, self.y * num)
