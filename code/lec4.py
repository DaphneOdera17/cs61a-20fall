def fib1(n):
    """Compute the nth Fibonacci number"""
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

def fib2(n):
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def square(x):
    return x * x

def inverse(f):
    """Return g(y) such that g(f(x)) -> x"""
    def inverse_of_f(y):
        def is_inverse_of_y(x):
            return f(x) == y
        return search(is_inverse_of_y)
    return inverse_of_f

    #return lambda y: search(lambda x: f(x) == y)

def compose1(f, g):
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

h = compose1(lambda x: x * x, lambda y: y + 1)
result1 = h(12) # 169
print(result1)

h = compose1(square, add_one)
result2 = h(12)
print(result2)

def compose2(f, g):
    def composed(x):
        return f(g(x))
    return composed

h = compose2(square, add_one)
result3 = h(12)
print(result3)

def make_adder(x):
    def adder(y):
        return x + y
    return adder

print(make_adder(1)(2))
f = make_adder(1)
print(f(2))

def f(y):
    return y + 1

g = lambda x: f
eight = g(2)(7)

g = lambda x: lambda y: y + 1
eight = g(2)(7)