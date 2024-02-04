def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a

def rational(n, d):
    """Construct a rational number x that represents n/d"""
    g = gcd(n, d)
    return [n // g, d // g]