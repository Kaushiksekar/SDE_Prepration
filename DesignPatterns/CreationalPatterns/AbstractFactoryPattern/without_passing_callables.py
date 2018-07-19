from decimal import Decimal

# f we prohibit our Python code from passing callables, then we eliminate verbs
#  from the arguments we can pass. Instead we will always pass nouns, and any
# verb we want to accomplish will have to dangle off of a noun as a method.
# Instead of a simple function, we’ll need to indent our code an extra level and
#  wrap it up inside a class.

class DecimalFactory(object):
    @staticmethod
    def build(string):
        return Decimal(string)

class Loader(object):
    @staticmethod
    def load(string, factory):
        string = string.lstrip(",") # allow trailing comma
        return [factory.build(item) for item in string.split(",")]

result = Loader.load("464.80, 933.68", DecimalFactory)
print(result)
