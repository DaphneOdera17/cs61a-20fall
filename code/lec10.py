def mysum(L):
    if (L == []):
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum([2, 4, 1, 5]))

def sum_rec(n):
    if n == 0:
        return 0
    else:
        return n + sum_rec(n - 1)

print(sum_rec(5))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'm', 'n', 'o', 'p']
a = [letters[i] for i in [3, 4, 6, 8]]
print(a)

odds = [1, 3, 5, 7, 9]
evens = [x + 1 for x in odds]
print(evens)

b = [x for x in odds if 25 % x == 0]
print(b)

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

print(divisors(12))

from operator import add
'curry = lambda f: lambda x: lambda y: f(x, y)'
exec('curry = lambda f: lambda x: lambda y: f(x, y)')
print(curry(add)(3)(4))

print('The Zen of Python\nclaims...\nRead')


# Reversing a List recursively
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

print(reverse('Hello World!'))

def fact_helper(n, k):
    """Computes k * (k + 1) * (k + 2) * ... * n"""
    if n == k:
        return n
    else:
        return k * fact_helper(n, k + 1)

def fact_(n):
    return fact_helper(n, 1)

print(fact_(5))