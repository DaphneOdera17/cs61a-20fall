from operator import floordiv, mod

def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

def prime_factors(n):
    """Print the prime factors of n in non-decreasing oder

    >>> prime_factors(4)
    2
    2
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(10)
    2
    5
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)

def smallest_prime_factor(n):
    """Return the smallest k > 1 that evenly divides n."""
    k = 2
    while n % k != 0:
        k += 1
    return k