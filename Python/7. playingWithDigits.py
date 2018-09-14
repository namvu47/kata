# integer n = abcd
# given p, find k so:
# a^p + b^(p+1) + c^(p+2) + d^(p+3) = n * k
# if k not exist, return -1

def dig_pow(n, p):
    _ln = {}
    _sum = 0
    for i in range (0,len(str(n))):
        _ln[i] = int(str(n)[i])
        _sum += _ln[i] ** (p+i)

    if _sum % n == 0:
        return _sum // n
    else:
        return -1
