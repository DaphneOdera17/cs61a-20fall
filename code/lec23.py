def fast_overlap(s, t):
    """Return the overlap between sorted S and sorted T.

    >>> fast_overlap([3, 4, 6, 7, 9, 10], [1, 3, 5, 7, 8])
    2
    """
    i, j, count = 0, 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i = i + 1
        else:
            j = j + 1
    return count

def stable(s, k, n):
    """Return whether all pairs of elements of S within
    distanc K differ by at most N.

    >>> stable([1, 2, 3, 5, 6], 1, 2)
    True
    >>> stable([1, 2, 3, 5 ,6], 2, 2)
    False
    >>> stable([1, 5, 1, 5, 1], 2, 2)
    False
    """

    for i in range(len(s)):
        near = range(max(0, i - k), i)
        if any([abs(s[i] - s[j]) > n for j in near]):
            return False
    return True