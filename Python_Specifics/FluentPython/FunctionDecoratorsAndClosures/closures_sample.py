# a higher order function to calculate a running average

def make_averager():
    series = []
    def average(new_value): # Within averager, series is a free variable, meaning it is not bound in the local scope
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return average

avg = make_averager()
print(avg(10))
print(avg(20))
print(avg(30))
print(avg)
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
# The binding for series is kept in the __closure__ attribute of the returned function
# avg. Each item in avg.__closure__ corresponds to a name in avg.__code__.co_free
# vars. These items are cells, and they have an attribute cell_contents where the actual
# value can be found
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
# To summarize: a closure is function that retains the bindings of the free variables that
# exist when the function is defined, so that they can be used later when the function is
# invoked and the defining scope is no longer available.
