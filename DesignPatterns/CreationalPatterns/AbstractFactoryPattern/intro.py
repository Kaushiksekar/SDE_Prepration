import json
from decimal import Decimal

text = '{"total": 9.61, "items": ["Americano", "Omelet"]}'

def build_decimal(string):
    return Decimal(string)

print(json.loads(text, parse_float=build_decimal))

# While the above code will certainly work, there is an elision we can perform
# thanks to the fact that Python types are themselves callables. The fact that
# Decimal is itself a callable taking a string argument and returning a decimal
# object instance means that, unless we need to edit the string first —
# for example, to removing a leading currency symbol — we can dispense with our
# own factory and simply pass the Decimal type directly to the JSON loader!

print("After elision")
print(json.loads(text, parse_float=Decimal))
