def make_averager():
    count = 0
    total = 0
    def average(value):
        nonlocal count, total # without this you'll get local var referenced before assignment error
        count += 1
        total += value
        return total / count
    return average

avg = make_averager()
print(avg(10))
print(avg(20))
print(avg(30))
