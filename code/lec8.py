def split(n):
    return n // 10, n % 10

all_but_last, last = split(2013)
print(all_but_last, last)

def sum_digits(n):
    """Return the sum of the digits of the positive integer n"""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
print(sum_digits(2013))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    