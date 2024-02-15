def plus_minus(x):
    """ generator
    >>> t = plus_minus(3)
    >>> next(t)
    3
    >>> next(t)
    -3
    """
    yield x
    yield -x


def evens(start, end):
    """
    >>> t = evens(2, 10)
    >>> next(t)
    2
    >>> next(t)
    4
    >>> next(t)
    6
    >>> next(t)
    8
    """
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

def a_then_b(a, b):
    """yield
    >>> list(a_then_b([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b_plus(a, b):
    """A yield from statement yields all values from
    an iterator or iterable
    """
    yield from a
    yield from b

def countdown(k):
    """countdown
    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    if k > 0:
        yield k
        yield from countdown(k - 1)
        # for x in countdown(k - 1):
        #   yield x

def prefixes(s):
    """prefixes
    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1]) # 不包括最后一个元素
        # for x in prefixes(s[:-1])
        #     yield x
        yield s

def substrings(s):
    """substrings
    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

def permutations(s):
    """permutation
    >>> list(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if len(s) == 0:
        yield []
    for i in range(len(s)):
        start = s[i] # 2
        rest = [s[j] for j in range(len(s)) if j != i] # [1, 3]
        # rest = s[:i] + s[i + 1:]
        for rest_permutation in permutations(rest):
            yield [start] + rest_permutation # [2, 1, 3] or [2, 3, 1]

def permutations_string(s):
    """string
    >>> list(permutations_string('abc'))
    ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    """
    if len(s) == 0:
        yield ''
    else:
        first = s[0]
        rest = s[1:]
        for rest_permutation in permutations_string(rest):
            for i in range(len(s)):
                yield rest_permutation[:i] + first + rest_permutation[i:]