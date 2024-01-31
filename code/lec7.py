def trace1(fn):
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1 # Function decorator
# Decorated function
def square(x):
    return x * x

@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total
sum_squares_up_to(5)

def repeat(k):
    """When called repeatedly, print each repeated argument

    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda j: False)(k)

def detector(f):
    def g(i):
        if f(i):
            print(i)
        return detector(lambda j: j == i or f(j))
    return g

f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)

# repeat                   (1)(7)(7)
# detector(lambda j: False)(1)(7)(7)
have_seen0 = lambda j: False
have_seen1 = lambda j: j == 1 or have_seen0(j)

ti = 1
timon = lambda y: y + ti
ti = -1
print(timon(5))