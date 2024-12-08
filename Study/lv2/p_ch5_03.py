# Closure 사용

def closure_ex1():
    series = []
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager

averager = closure_ex1()

print(averager(10))
print(averager(10))
print(averager(10))
print(averager(10))

# function inspection
# print(dir(averager))

# print(dir(averager.__code__))
print(averager.__code__.co_freevars)
print(averager.__closure__[0].cell_contents)