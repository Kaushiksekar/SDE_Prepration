from decimal import Decimal

class Factory(object):
    def build_number(self, string):
        return Decimal(string)
    def build_sequence(self):
        return []

class Loader(object):
    @staticmethod
    def load(string, factory):
        sequence = factory.build_sequence()
        for substring in string.split(","):
            item = factory.build_number(substring)
            sequence.append(item)
        return sequence

f = Factory()
result = Loader.load("1.23, 4.56", f)
print(result)

#Second, consider the behavior of languages that force you to declare ahead of
# time the type of each method parameter. You would overly restrict your future
# choices if your code insisted that the factory parameter could only ever be an
# instance of this particular class Factory because then you could never pass in
#  anything that didn’t inherit from it.

# Instead, to more happily separate specification from implementation, you would
# create an abstract class. It’s this final step that merits the word “abstract”
# in the pattern’s name “Abstract Factory”. Your abstract class would merely
# promise that the factory argument to load() would be a class adhering to the
# required interface
