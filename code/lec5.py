def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

result = repeat(g, 5)

def make_adder(n):
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
result = add_three(4)

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    """
    :param f:
    :param g:
    :return:

    >>> squiple = compose1(square, triple)
    >>> squiple(5)
    225
    """
    def h(x):
        return f(g(x))
    return h

compose1(square, make_adder(2))(3) # 25

def print_all(x):
    print(x)
    return print_all

f = print_all(1) # 将打印 1，并且该表达式的值将作为 print_all 函数
f(3)
print_all(2)(4)(6)

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x + y)
    return next_sum

print_sums(1)(3)(5)

def make_adder_plus(n):
    return lambda k: n + k

make_adder_plus(2)(3) # 5

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

from operator import add
curry2_plus = lambda f: lambda x: lambda y: f(x, y)
m = curry2_plus(add)
m(2)(3)