def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield b
list(a_then_b([3, 4], [5, 6]))
# [3, 4, 5, 6]

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
    else:
        yield 'Blast of f'

def prefixes(s):
    if s:
        # for x in prefixes(s[:-1])
        #     yield x
        yield from prefixes(s[:-1])
        yield s
def prefixes_(s):
     result = []
     if s:
        for x in prefixes_(s[:-1]):
            result.append(x)
        result.append(s)
     return result
print(list(prefixes_('dogs')))

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

list(substrings('tops'))