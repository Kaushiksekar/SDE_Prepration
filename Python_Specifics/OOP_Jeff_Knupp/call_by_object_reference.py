def list_add(b):
    b.append(5)

def string_add(a):
    a += "xcxc"

a = [1,2,3,4]
print(a)
list_add(a)
print(a)

b = "asdasds" #immutable
print(b)
string_add(b)
print(b)
