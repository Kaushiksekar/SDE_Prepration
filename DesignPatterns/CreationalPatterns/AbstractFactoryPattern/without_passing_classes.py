from decimal import Decimal

class DecimalFactory(object):
    def build(self, string):
        return Decimal(string)

class Loader(object):
    @staticmethod
    def load(string, factory):
        string = string.lstrip(",")
        return [factory.build(item) for item in string.split(",")]

f = DecimalFactory()
result = Loader.load("464.80, 993.68", f)
print(result)
