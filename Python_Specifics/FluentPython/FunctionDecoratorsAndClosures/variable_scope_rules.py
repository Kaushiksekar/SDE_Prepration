b=3
def f1(a):
    print(a)
    print(b)

f1(4)

def f2(a): # in this case we get an error for b as it is also a local scope
    print(a) # this is because python compiles the function and notes that a and b are in local scope
    print(b) # and when f2 is called, b is unbound
    b=5

# f2(6)

#the above scenario is solved by using global
def f3(a): # in here however, b is fetched from global scope and when value of b is changed, the new value applies at the global scope
    print(a)
    global b
    print(b)
    b = 9
    print(b)

f3(15)
